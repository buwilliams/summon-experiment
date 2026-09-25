import copy
import tempfile
import time
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from summon.markdown import render_markdown
from summon.web import create_app


class Gateway:
    def chat(self, messages):
        return {"role": "assistant", "content": "## Recommendation\n\n**Run a pilot.**\n\n- Measure results\n- Review costs"}, {}

    def judge(self, scenario, answers):
        return {"answer_1": .7, "answer_2": .3}, {}


class StudyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name)
        self.app = create_app(self.path, Gateway())
        self.client = TestClient(self.app)
        c = self.client.get('/api/state').json()['catalog']
        c['views'] = c['views'][:1]
        c['views'][0]['styles'] = c['views'][0]['styles'][:2]
        first = c['experiments'][0]
        first['view_ids'] = [c['views'][0]['id']]
        c['hypotheses'].append(dict(id='another-hypothesis', name='Another hypothesis', statement='A different statement.'))
        c['experiments'] = c['experiments'][:2]
        c['experiments'][1].update(id='another-study', hypothesis_id='another-hypothesis', name='Another experiment', view_ids=first['view_ids'])
        response = self.client.put('/api/catalog', json=c)
        self.assertEqual(response.status_code, 200, response.text)
        self.catalog = response.json()

    def tearDown(self):
        self.tmp.cleanup()

    def collect_report(self):
        batch = self.client.post('/api/batches', params={'experiment_id': self.catalog['experiments'][0]['id']}).json()
        for _ in range(2):
            session = self.client.post('/api/interview/next', params={'batch_id': batch['id']}).json()
            response = self.client.post(f"/api/sessions/{session['id']}/submit", json={'message': 1})
            self.assertEqual(response.status_code, 200, response.text)
        response = self.client.post(f"/api/batches/{batch['id']}/reports")
        self.assertEqual(response.status_code, 200, response.text)
        rid = response.json()[0]['id']
        for _ in range(100):
            report = self.app.state.store.get('report', rid)
            if report['status'] != 'running':
                break
            time.sleep(.02)
        self.assertEqual(report['status'], 'complete')
        return batch, report

    def test_study_scopes_and_frozen_provenance(self):
        batch = self.client.post('/api/batches', params={'experiment_id': 'another-study'}).json()
        self.assertEqual(batch['hypothesis']['id'], 'another-hypothesis')
        self.assertEqual(len(batch['catalog']['scenarios']), 1)
        self.assertEqual(batch['catalog']['scenarios'][0]['id'], self.catalog['experiments'][1]['id'])
        self.assertEqual(self.client.get('/api/batches').json()[0]['total'], 2)
        c = copy.deepcopy(self.catalog)
        c['experiments'][1]['name'] = 'Renamed study'
        c['experiments'][1]['text'] = 'Changed case text'
        self.assertEqual(self.client.put('/api/catalog', json=c).status_code, 200)
        session = self.client.post('/api/interview/next', params={'batch_id': batch['id']}).json()
        self.assertEqual(session['experiment']['name'], 'Another experiment')
        self.assertEqual(session['scenario']['id'], self.catalog['experiments'][1]['id'])
        path = self.app.state.store._path('session', session)
        self.assertIn('hypotheses', path.parts)
        self.assertIn('experiments', path.parts)
        self.assertIn('batches', path.parts)
        self.assertIn('tests', path.parts)
        self.assertEqual(self.client.post('/api/batches', params={'experiment_id': 'missing'}).status_code, 400)

    def test_invalid_parent_or_scope_is_rejected(self):
        for field, value in [('hypothesis_id', 'missing'), ('text', ''), ('view_ids', [])]:
            c = copy.deepcopy(self.catalog)
            c['experiments'][0][field] = value
            self.assertEqual(self.client.put('/api/catalog', json=c).status_code, 400)

    def test_anonymous_judgments_survive_restart_and_do_not_change_jev(self):
        _, report = self.collect_report()
        url = f"/api/reports/{report['id']}/ballots"
        data = self.client.post(url, json={'reviewer': 'Buddy'}).json()
        self.assertEqual(data['total'], 1)
        ballot = data['ballots'][0]
        self.assertNotIn('jev', ballot)
        self.assertNotIn('identities', ballot)
        self.assertNotIn('display_order', ballot)
        self.assertEqual([r['label'] for r in ballot['responses']], ['A', 'B'])
        self.assertIn('<h2>', ballot['responses'][0]['html'])
        again = self.client.post(url, json={'reviewer': 'buddy'}).json()
        self.assertEqual(again['ballots'][0]['id'], ballot['id'])
        original = copy.deepcopy(report)
        saved = self.client.post(f"/api/ballots/{ballot['id']}/vote", json={'reviewer': 'Buddy', 'choice': 'A', 'reason': 'Clearer reasons.'})
        self.assertEqual(saved.status_code, 200, saved.text)
        self.assertIn('jev', saved.json())
        self.assertIn('identities', saved.json())
        self.assertEqual(self.app.state.store.get('report', report['id']), original)
        conflict = self.client.post(f"/api/ballots/{ballot['id']}/vote", json={'reviewer': 'Buddy', 'choice': 'B'})
        self.assertEqual(conflict.status_code, 409)
        duplicate = self.client.post(f"/api/ballots/{ballot['id']}/vote", json={'reviewer': 'buddy', 'choice': 'A', 'reason': 'Clearer reasons.'})
        self.assertEqual(duplicate.status_code, 200)
        second = self.client.post(url, json={'reviewer': 'Reviewer two'}).json()['ballots'][0]
        self.assertEqual(self.client.post(f"/api/ballots/{second['id']}/vote", json={'reviewer': 'Buddy', 'choice': 'tie'}).status_code, 400)
        self.client.post(f"/api/ballots/{second['id']}/vote", json={'reviewer': 'Reviewer two', 'choice': 'tie'})
        restarted = TestClient(create_app(self.path, Gateway()))
        resumed = restarted.post(url, json={'reviewer': 'Buddy'}).json()
        self.assertEqual(resumed['completed'], 1)
        self.assertEqual(resumed['ballots'][0]['choice'], 'A')
        summary = restarted.get('/api/state').json()['reports'][0]['human']
        self.assertEqual((summary['votes'], summary['reviewers'], summary['judged_pairs']), (2, 2, 1))
        self.assertEqual(summary['agreement'], 1)  # Jev ties after order balancing; only human tie agrees.
        self.assertEqual(sorted(summary['pairs'][0]['scores'].values()), [.25, .75])
        self.assertEqual(len(list(self.path.glob('hypotheses/**/judgments/*.md'))), 2)
        exported = restarted.get('/api/export').json()
        self.assertEqual(len(exported['human_judgments']), 2)
        self.assertTrue(all(b['display_order'] for b in exported['human_judgments']))

    def test_markdown_is_display_only_and_cannot_execute_html(self):
        text = '# Heading\n\n**Bold** and *italic*.\n\n- Item\n\n```python\nprint(1)\n```\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n<script>alert(1)</script>\n\n[bad](javascript:alert(1))\n\n![image](https://tracker.example/pixel)'
        html = render_markdown(text)
        for tag in ['<h1>', '<strong>', '<em>', '<ul>', '<pre>', '<table>']:
            self.assertIn(tag, html)
        self.assertNotIn('<script>', html)
        self.assertNotIn('href="javascript:', html)
        self.assertNotIn('<img', html)
        batch, report = self.collect_report()
        state = self.client.get('/api/state').json()
        self.assertIn('<strong>', state['sessions'][0]['messages'][1]['html'])
        stored = self.app.state.store.get('session', state['sessions'][0]['id'])
        self.assertNotIn('html', stored['messages'][1])
        self.assertTrue(report['submissions'][0]['text'].startswith('## Recommendation'))


if __name__ == '__main__':
    unittest.main()

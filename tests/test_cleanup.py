import json
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from summon.cleanup import CleanupInput
from summon.web import create_app


class FakeGateway:
    def chat(self, messages):
        return {"role": "assistant", "content": "A test recommendation."}, {}

    def judge(self, scenario, answers):
        return {"answer_1": .6, "answer_2": .4}, {}


class CleanupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'records'
        self.app = create_app(self.root, FakeGateway())
        self.client = TestClient(self.app)
        self.store = self.app.state.store
        c = self.client.get('/api/state').json()['catalog']
        c['experiments'] = c['experiments'][:1]
        c['views'] = c['views'][:1]
        c['views'][0]['styles'] = c['views'][0]['styles'][:2]
        c['experiments'][0]['view_ids'] = [c['views'][0]['id']]
        self.assertEqual(self.client.put('/api/catalog', json=c).status_code, 200)
        self.batch = self.client.post('/api/batches').json()

    def tearDown(self):
        self.tmp.cleanup()

    def collect(self):
        tests = []
        for _ in range(2):
            s = self.client.post('/api/interview/next', params={'batch_id': self.batch['id']}).json()
            self.assertEqual(self.client.post(f"/api/sessions/{s['id']}/submit", json={'message': 1}).status_code, 200)
            tests.append(s)
        r = self.client.post(f"/api/batches/{self.batch['id']}/reports").json()[0]
        for _ in range(100):
            r = self.store.get('report', r['id'])
            if r['status'] != 'running':
                break
            time.sleep(.02)
        self.assertEqual(r['status'], 'complete')
        ballot = self.client.post(f"/api/reports/{r['id']}/ballots", json={'reviewer': 'Tester'}).json()['ballots'][0]
        self.client.post(f"/api/ballots/{ballot['id']}/vote", json={'reviewer': 'Tester', 'choice': 'A'})
        return tests, r

    def cleanup(self, scope, id=None):
        selected = dict(scope=scope, id=id)
        preview = self.client.post('/api/data/preview', json=selected)
        self.assertEqual(preview.status_code, 200, preview.text)
        result = self.client.post('/api/data/cleanup', json={**selected, 'fingerprint': preview.json()['fingerprint']})
        self.assertEqual(result.status_code, 200, result.text)
        return result.json()

    def test_all_cleanup_and_restart_restore_preserve_exact_files(self):
        self.collect()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        a = self.cleanup('all')
        counts = self.client.get('/api/data').json()['counts']
        self.assertTrue(all(value == 0 for value in counts.values()))
        self.assertTrue(list((self.root / 'catalog').glob('*.json')))
        self.assertTrue((self.store.cleanup.trash / (a['id'] + '.json')).exists())
        restarted = TestClient(create_app(self.root, FakeGateway()))
        self.assertEqual(restarted.post(f"/api/data/trash/{a['id']}/restore").status_code, 200)
        for relative, content in before.items():
            self.assertEqual((self.root / relative).read_bytes(), content)
        self.assertEqual(restarted.post(f"/api/data/trash/{a['id']}/restore").status_code, 200)
        self.assertEqual(restarted.get('/api/data').json()['trash'], [])

    def test_test_family_removes_dependencies_and_resets_only_that_cell(self):
        tests, report = self.collect()
        revision = self.client.post(f"/api/sessions/{tests[0]['id']}/revise").json()
        self.client.post(f"/api/sessions/{revision['id']}/submit", json={'message': 1})
        a = self.cleanup('test', revision['id'])
        self.assertEqual(a['counts'], dict(batch=0, session=2, submission=2, report=1, ballot=1))
        progress = self.client.get('/api/batches').json()[0]
        self.assertEqual((progress['completed'], progress['total']), (1, 2))
        self.assertEqual(len(self.store.all('session')), 1)
        self.assertEqual(self.client.post(f"/api/data/trash/{a['id']}/restore").status_code, 200)
        self.assertEqual(self.client.get('/api/batches').json()[0]['completed'], 2)

    def test_report_restore_requires_parent_data_and_does_not_overwrite(self):
        _, report = self.collect()
        a = self.cleanup('report', report['id'])
        self.assertEqual(a['counts']['report'], 1)
        self.assertEqual(a['counts']['session'], 0)
        b = self.cleanup('batch', self.batch['id'])
        self.assertEqual(self.client.post(f"/api/data/trash/{a['id']}/restore").status_code, 409)
        self.assertEqual(self.client.post(f"/api/data/trash/{b['id']}/restore").status_code, 200)
        self.assertEqual(self.client.post(f"/api/data/trash/{a['id']}/restore").status_code, 200)
        a = self.cleanup('report', report['id'])
        report['name'] = 'Changed report'
        self.store.put('report', report)
        self.assertEqual(self.client.post(f"/api/data/trash/{a['id']}/restore").status_code, 409)
        self.assertEqual(self.store.get('report', report['id'])['name'], 'Changed report')

    def test_stale_preview_rejected_and_batch_names_not_reused(self):
        preview = self.client.post('/api/data/preview', json={'scope': 'all'}).json()
        self.client.post('/api/interview/next', params={'batch_id': self.batch['id']})
        self.assertEqual(self.client.post('/api/data/cleanup', json={'scope': 'all', 'fingerprint': preview['fingerprint']}).status_code, 409)
        a = self.cleanup('batch', self.batch['id'])
        new = self.client.post('/api/batches').json()
        self.assertNotEqual(new['name'], self.batch['name'])
        self.assertEqual(self.client.post(f"/api/data/trash/{a['id']}/restore").status_code, 200)
        self.assertEqual(len(self.store.all('batch')), 2)

    def test_interrupted_cleanup_finishes_on_restart(self):
        self.collect()
        data = CleanupInput(scope='all')
        data.fingerprint = self.store.cleanup.plan(data)['fingerprint']
        original = Path.unlink
        removed = []
        def interrupted(path, *args, **kwargs):
            if path.suffix == '.md' and path.is_relative_to(self.root):
                raise OSError('Simulated interruption')
            removed.append(path)
            return original(path, *args, **kwargs)
        with patch.object(Path, 'unlink', interrupted):
            with self.assertRaises(OSError):
                self.store.cleanup.remove(data)
        self.assertTrue(self.store.failed)
        self.assertTrue(removed)
        restarted = create_app(self.root, FakeGateway())
        self.assertEqual(restarted.state.store.all('batch'), [])
        self.assertEqual(restarted.state.store.all('session'), [])
        archive = restarted.state.store.cleanup.archives()[0]
        self.assertEqual(archive['status'], 'trashed')
        self.assertEqual(TestClient(restarted).post(f"/api/data/trash/{archive['id']}/restore").status_code, 200)

    def test_judgments_only_and_path_protection(self):
        self.collect()
        a = self.cleanup('judgments')
        self.assertEqual(a['counts'], dict(batch=0, session=0, submission=0, report=0, ballot=1))
        self.assertEqual(len(self.store.all('report')), 1)
        for path in ['../outside.json', 'catalog/revision-000001.json', '.env', str(self.root.parent / 'outside.json')]:
            with self.assertRaises(ValueError):
                self.store.cleanup.checked_path(path)

    def test_experiment_cleanup_keeps_other_studies_and_definitions(self):
        c = self.client.get('/api/state').json()['catalog']
        c['experiments'].append({**c['experiments'][0], 'id': 'other-study', 'name': 'Other study'})
        self.assertEqual(self.client.put('/api/catalog', json=c).status_code, 200)
        other = self.client.post('/api/batches', params={'experiment_id': 'other-study'}).json()
        definitions = {p.name: p.read_bytes() for p in (self.root / 'catalog').iterdir()}
        self.cleanup('experiment', self.batch['experiment']['id'])
        self.assertEqual([b['id'] for b in self.store.all('batch')], [other['id']])
        self.assertEqual(definitions, {p.name: p.read_bytes() for p in (self.root / 'catalog').iterdir()})

    def test_interrupted_restore_finishes_on_restart(self):
        self.collect()
        archive = self.cleanup('all')
        original = self.store._atomic
        def interrupted(path, text):
            if path.name == 'session.md':
                raise OSError('Interrupted restore')
            return original(path, text)
        with patch.object(self.store, '_atomic', interrupted):
            with self.assertRaises(OSError):
                self.store.cleanup.restore(archive['id'])
        restored = create_app(self.root, FakeGateway()).state.store
        self.assertEqual(len(restored.all('session')), 2)
        self.assertEqual(len(restored.all('report')), 1)
        self.assertEqual(len(restored.all('ballot')), 1)
        self.assertEqual(restored.cleanup.archives()[0]['status'], 'restored')

    def test_cleanup_waits_for_inflight_model_request(self):
        started, release = threading.Event(), threading.Event()
        class Slow(FakeGateway):
            def chat(self, messages):
                started.set()
                release.wait(10)
                return super().chat(messages)
        client = TestClient(create_app(Path(self.tmp.name) / 'busy-data', Slow()))
        worker = threading.Thread(target=lambda: client.post('/api/interview/next'))
        worker.start()
        try:
            self.assertTrue(started.wait(5))
            response = client.post('/api/data/preview', json={'scope': 'all'})
            self.assertEqual(response.status_code, 409)
            self.assertIn('Wait for current model requests', response.json()['detail'])
        finally:
            release.set()
            worker.join(10)


if __name__ == '__main__':
    unittest.main()

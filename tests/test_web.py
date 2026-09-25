import tempfile
import time
import unittest
from pathlib import Path
from fastapi.testclient import TestClient
from summon.web import create_app, Gateway


class FakeGateway:
    def __init__(self):
        self.calls = []
        self.chat_inputs = []
        self.fail = False

    def chat(self, messages):
        self.chat_inputs.append(messages)
        if self.fail:
            raise ValueError("Temporary failure")
        return {"role": "assistant", "content": "Solution " + messages[-1]["content"]}, {"usage": {"total_tokens": 5}}

    def judge(self, scenario, answers):
        if self.fail:
            raise ValueError("Temporary failure")
        self.calls.append((scenario, answers))
        return {"answer_1": .7, "answer_2": .3}, {"model": "fake"}


class WebTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.g = FakeGateway()
        self.app = create_app(Path(self.tmp.name) / "experiment-data", self.g)
        self.client = TestClient(self.app)
        self.catalog = self.client.get("/api/state").json()["catalog"]

    def tearDown(self):
        self.tmp.cleanup()

    def session(self, view=0, style=0):
        c = self.catalog
        r = self.client.post("/api/sessions", json=dict(scenario=c["experiments"][0]["id"],
            view=c["views"][view]["id"], style=c["views"][view]["styles"][style]["id"], participant="Tester", batch="Test"))
        self.assertEqual(r.status_code, 200)
        return r.json()["id"]

    def submission(self, view=0, style=0):
        id = self.session(view, style)
        self.assertEqual(self.client.post(f"/api/sessions/{id}/messages", json={"text": "My prompt"}).status_code, 200)
        return self.client.post(f"/api/sessions/{id}/submit", json={"message": 1}).json()

    def wait(self, id):
        for _ in range(100):
            r = self.app.state.store.get("report", id)
            if r["status"] != "running":
                return r
            time.sleep(.03)
        self.fail("Report did not finish")

    def test_independent_lab_question_belongs_to_each_style_only(self):
        c = self.catalog
        lab = next(s for s in c["experiments"] if s["name"] == "Independent Lab")
        other = next(s for s in c["experiments"] if s["name"] == "Legacy Rewrite")
        question = "Which strategy is right?"
        self.assertNotIn(question, lab["text"])
        self.assertIn(question, other["text"])
        for view in c["views"]:
            for style in view["styles"]:
                for scenario in (lab, other):
                    session = self.client.post("/api/sessions", json=dict(
                        experiment_id=scenario["id"], scenario=scenario["id"], view=view["id"], style=style["id"], participant="Tester", batch="Test"
                    )).json()
                    self.assertEqual(question in session["style"]["opening"], scenario == lab)
                    result = self.client.post(f"/api/sessions/{session['id']}/opening")
                    self.assertEqual(result.status_code, 200)
                    prompt = self.g.chat_inputs[-1][0]["content"]
                    self.assertEqual(prompt.count(question), 1)
                    self.assertEqual(question in prompt.split("Test:")[0], scenario == other)

    def test_retired_guidance_is_not_seeded_saved_or_reintroduced(self):
        self.assertTrue(all("guidance" not in s for v in self.catalog["views"] for s in v["styles"]))
        self.catalog["views"][0]["styles"][0]["guidance"] = "Legacy field from a stale editor"
        saved = self.client.put("/api/catalog", json=self.catalog)
        self.assertEqual(saved.status_code, 200)
        self.assertNotIn("guidance", saved.json()["views"][0]["styles"][0])
        legacy = saved.json()
        legacy["views"][0]["styles"][0]["guidance"] = "Old catalog"
        self.app.state.store.put("catalog", legacy)
        restarted = create_app(self.app.state.store.path, self.g)
        upgraded = restarted.state.store.get("catalog", "catalog")
        self.assertEqual(upgraded["revision"], legacy["revision"] + 1)
        self.assertNotIn("guidance", upgraded["views"][0]["styles"][0])
        self.assertEqual(upgraded["views"][0]["styles"][0]["opening"], legacy["views"][0]["styles"][0]["opening"])

    def test_failure_retains_prompt_and_submission_freezes_response(self):
        id = self.session()
        self.g.fail = True
        self.assertEqual(self.client.post(f"/api/sessions/{id}/messages", json={"text": "retry me"}).status_code, 400)
        s = self.app.state.store.get("session", id)
        self.assertEqual(s["pending"], "retry me")
        self.assertEqual(s["messages"], [])
        self.g.fail = False
        self.client.post(f"/api/sessions/{id}/messages", json={"text": "retry me"})
        self.assertEqual(self.client.post(f"/api/sessions/{id}/submit", json={"message": 0}).status_code, 400)
        self.assertEqual(self.client.post(f"/api/sessions/{id}/submit", json={"message": 1}).status_code, 200)
        self.assertEqual(self.client.post(f"/api/sessions/{id}/messages", json={"text": "later"}).status_code, 409)
        self.assertEqual(self.client.post(f"/api/sessions/{id}/submit", json={"message": 1}).status_code, 409)

    def test_interview_automatically_assigns_resumes_and_advances(self):
        first = self.client.post('/api/interview/next').json()
        self.assertEqual(self.client.post('/api/interview/next').json()['id'], first['id'])
        self.client.post(f"/api/sessions/{first['id']}/messages", json={'text': 'Question'})
        self.client.post(f"/api/sessions/{first['id']}/submit", json={'message': 1})
        second = self.client.post('/api/interview/next').json()
        self.assertNotEqual(first['id'], second['id'])
        self.assertEqual(first['batch'], second['batch'])
        self.assertNotEqual(tuple(first[k]['id'] for k in ['scenario','view','style']),
                            tuple(second[k]['id'] for k in ['scenario','view','style']))

    def test_interview_resumes_existing_manual_session(self):
        id = self.session()
        self.assertEqual(self.client.post('/api/interview/next').json()['id'], id)

    def test_automatic_opening_contains_assignment_once_and_is_not_repeated(self):
        session = self.client.post('/api/interview/next').json()
        self.assertEqual(len(self.g.chat_inputs), 1)
        sent = self.g.chat_inputs[0]
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0]['role'], 'user')
        for text in [session['scenario']['text'], session['view']['name'], session['style']['name']]:
            self.assertIn(text, sent[0]['content'])
        self.assertEqual(sent[0]['content'].count(session['scenario']['text']), 1)
        self.assertEqual(session['initial_prompt'], sent[0]['content'])
        self.client.post('/api/interview/next')
        self.client.post(f"/api/sessions/{session['id']}/opening")
        self.assertEqual(len(self.g.chat_inputs), 1)
        self.client.post(f"/api/sessions/{session['id']}/messages", json={'text':'Why that recommendation?'})
        self.assertEqual(len(self.g.chat_inputs[-1]), 3)
        self.assertEqual(self.g.chat_inputs[-1][0], sent[0])

    def test_failed_automatic_opening_can_resume_without_duplicate_interview(self):
        self.g.fail = True
        self.assertEqual(self.client.post('/api/interview/next').status_code, 400)
        session = self.app.state.store.all('session')[0]
        self.assertEqual(session['messages'], [])
        self.assertEqual(session['pending'], session['initial_prompt'])
        self.g.fail = False
        recovered = self.client.post('/api/interview/next').json()
        self.assertEqual(recovered['id'], session['id'])
        self.assertEqual(len(recovered['messages']), 2)
        self.assertEqual(len(self.app.state.store.all('session')), 1)

    def test_batches_start_fresh_switch_resume_and_freeze_roster(self):
        first = self.client.post('/api/batches').json()
        one = self.client.post('/api/interview/next', params={'batch_id': first['id']}).json()
        second = self.client.post('/api/batches').json()
        two = self.client.post('/api/interview/next', params={'batch_id': second['id']}).json()
        self.assertNotEqual(one['batch'], two['batch'])
        self.assertEqual(len(two['messages']), 2)
        self.assertEqual(self.client.post('/api/interview/next', params={'batch_id': first['id']}).json()['id'], one['id'])
        self.catalog['experiments'] = self.catalog['experiments'][:1]
        for experiment in self.catalog['experiments']:
            experiment['view_ids'] = [v['id'] for v in self.catalog['views']]
        self.assertEqual(self.client.put('/api/catalog', json=self.catalog).status_code, 200)
        old = next(b for b in self.client.get('/api/batches').json() if b['id'] == first['id'])
        self.assertEqual(old['total'], 15)
        self.assertEqual(old['in_progress'], 1)
        self.assertEqual(old['completed'], 0)
        self.client.post(f"/api/sessions/{one['id']}/messages", json={'text':'A question'})
        self.client.post(f"/api/sessions/{one['id']}/submit", json={'message':1})
        following = self.client.post('/api/interview/next', params={'batch_id': first['id']}).json()
        self.assertEqual(following['revision'], 1)

    def test_revision_preserves_original_and_replaces_only_future_submission(self):
        sub = self.submission()
        before = self.client.get('/api/batches').json()[0]
        original = self.app.state.store.get('session', sub['session'])
        self.assertEqual(before['completed'], 1)
        draft = self.client.post(f"/api/sessions/{sub['session']}/revise").json()
        self.assertNotEqual(draft['id'], original['id'])
        self.assertEqual(draft['messages'], original['messages'])
        self.assertEqual(self.client.post(f"/api/sessions/{sub['session']}/revise").json()['id'], draft['id'])
        progress = self.client.get('/api/batches').json()[0]
        self.assertEqual((progress['completed'], progress['in_progress']), (0, 1))
        self.client.post(f"/api/sessions/{draft['id']}/messages", json={'text':'Summarize your recommendation'})
        updated = self.client.post(f"/api/sessions/{draft['id']}/submit", json={'message':3}).json()
        self.assertEqual(updated['replaces'], sub['id'])
        self.assertEqual(self.app.state.store.get('session', original['id']), original)
        old = self.app.state.store.get('submission', sub['id'])
        self.assertEqual(old['text'], sub['text'])
        self.assertFalse(old['included'])
        self.assertEqual(old['superseded_by'], updated['id'])
        self.assertEqual(self.client.get('/api/batches').json()[0]['completed'], 1)

    def test_completed_batch_does_not_silently_start_new_round(self):
        self.catalog['experiments'] = self.catalog['experiments'][:1]
        self.catalog['views'] = self.catalog['views'][:1]
        self.catalog['views'][0]['styles'] = self.catalog['views'][0]['styles'][:1]
        for experiment in self.catalog['experiments']:
            experiment['view_ids'] = [v['id'] for v in self.catalog['views']]
        self.assertEqual(self.client.put('/api/catalog', json=self.catalog).status_code, 200)
        batch = self.client.post('/api/batches').json()
        session = self.client.post('/api/interview/next', params={'batch_id':batch['id']}).json()
        self.client.post(f"/api/sessions/{session['id']}/messages", json={'text':'Recommend'})
        self.client.post(f"/api/sessions/{session['id']}/submit", json={'message':1})
        end = self.client.post('/api/interview/next', params={'batch_id':batch['id']}).json()
        self.assertTrue(end['complete'])
        progress = self.client.get('/api/batches').json()[0]
        self.assertEqual((progress['completed'], progress['total']), (1, 1))

    def test_dated_batch_names_and_legacy_migration_are_stable(self):
        id = self.session()
        original = self.app.state.store.get('session', id)
        one = self.client.get('/api/batches').json()[0]
        self.assertRegex(one['name'], r'^Batch \d{8}-1$')
        two = self.client.post('/api/batches').json()
        self.assertEqual(two['name'], one['name'][:-1] + '2')
        batches = self.client.get('/api/batches').json()
        self.assertEqual(len(batches), 2)
        migrated = self.app.state.store.get('session', id)
        self.assertEqual(migrated['batch'], one['name'])
        self.assertEqual(migrated['messages'], original['messages'])
        self.assertEqual(migrated['id'], original['id'])
        self.assertEqual(self.client.post('/api/interview/next', params={'batch_id':one['id']}).json()['id'], id)

    def test_batch_runner_validates_all_inputs_for_one_experiment(self):
        self.catalog['experiments'] = self.catalog['experiments'][:2]
        self.catalog['views'] = self.catalog['views'][:1]
        self.catalog['views'][0]['styles'] = self.catalog['views'][0]['styles'][:2]
        for experiment in self.catalog['experiments']:
            experiment['view_ids'] = [v['id'] for v in self.catalog['views']]
        self.assertEqual(self.client.put('/api/catalog', json=self.catalog).status_code, 200)
        batch = self.client.post('/api/batches').json()
        url = f"/api/batches/{batch['id']}/reports"
        self.assertEqual(self.client.post(url).status_code, 400)
        submissions = []
        for _ in range(2):
            session = self.client.post('/api/interview/next', params={'batch_id':batch['id']}).json()
            self.client.post(f"/api/sessions/{session['id']}/messages", json={'text':'Recommend'})
            submissions.append(self.client.post(f"/api/sessions/{session['id']}/submit", json={'message':1}).json())
        self.client.patch('/api/submissions/'+submissions[-1]['id'], json={'included':False})
        self.assertEqual(self.client.post(url).status_code, 400)
        self.assertEqual(self.g.calls, [])
        self.assertEqual(self.app.state.store.all('report'), [])
        self.client.patch('/api/submissions/'+submissions[-1]['id'], json={'included':True})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200, response.text)
        reports = response.json()
        self.assertEqual(len(reports), 1)
        for r in reports:
            result = self.wait(r['id'])
            self.assertEqual(result['status'], 'complete')
            self.assertEqual(result['batch_id'], batch['id'])
            self.assertEqual(len({s['scenario']['id'] for s in result['submissions']}), 1)
        self.assertEqual(len(self.g.calls), 2)

    def test_round_robin_balances_order_and_advances_ties(self):
        subs = [self.submission(v, t) for v in range(2) for t in range(5)]
        r = self.client.post("/api/reports", json={"name": "test", "submissions": [s["id"] for s in subs]})
        self.assertEqual(r.status_code, 200, r.text)
        result = self.wait(r.json()["id"])
        self.assertEqual(result["status"], "complete")
        self.assertEqual(len([p for p in result["pairs"] if p["stage"] == "within"]), 20)
        # Position-only preference disappears after order balancing; all ties advance.
        self.assertEqual(len([p for p in result["pairs"] if p["stage"] == "cross"]), 25)
        self.assertTrue(all(score == .5 for p in result["pairs"] for score in p["scores"].values()))
        self.assertEqual(len(self.g.calls), 90)
        self.assertTrue(all(set(answers) == {"answer_1", "answer_2"} for _, answers in self.g.calls))

    def test_incomplete_view_rejected_and_resume_does_not_repeat_calls(self):
        subs = [self.submission(0, t) for t in range(5)]
        self.assertEqual(self.client.post("/api/reports", json={"name": "partial", "submissions": [s["id"] for s in subs[:2]]}).status_code, 400)
        self.g.fail = True
        r = self.client.post("/api/reports", json={"name": "test", "submissions": [s["id"] for s in subs]}).json()
        self.assertEqual(self.wait(r["id"])["status"], "failed")
        self.g.fail = False
        self.client.post(f"/api/reports/{r['id']}/resume")
        self.assertEqual(self.wait(r["id"])["status"], "complete")
        self.assertEqual(len(self.g.calls), 20)
        self.assertEqual(self.client.post(f"/api/reports/{r['id']}/resume").status_code, 409)

    def test_revision_snapshot_and_cross_origin_protection(self):
        id = self.session()
        old = self.catalog["experiments"][0]["text"]
        self.catalog["experiments"][0]["text"] = "New scenario"
        self.assertEqual(self.client.put("/api/catalog", json=self.catalog).status_code, 200)
        self.assertEqual(self.client.put("/api/catalog", json=self.catalog).status_code, 409)
        self.assertEqual(self.app.state.store.get("session", id)["scenario"]["text"], old)
        self.assertEqual(self.client.post("/api/sessions", json={}, headers={"origin": "https://untrusted.example"}).status_code, 403)

    def test_resume_preserves_first_order_checkpoint(self):
        subs = [self.submission(0, t) for t in range(5)]
        judge = self.g.judge
        def fail_second(scenario, answers):
            if len(self.g.calls) == 1:
                raise ValueError("Second call failed")
            return judge(scenario, answers)
        self.g.judge = fail_second
        r = self.client.post("/api/reports", json={"name": "checkpoint", "submissions": [s["id"] for s in subs]}).json()
        failed = self.wait(r["id"])
        self.assertEqual(failed["status"], "failed")
        self.assertEqual(len(failed["pairs"][0]["orders"]), 1)
        self.g.judge = judge
        self.client.post(f"/api/reports/{r['id']}/resume")
        result = self.wait(r["id"])
        self.assertEqual(result["status"], "complete")
        self.assertEqual(len(self.g.calls), 20)
        self.assertEqual(result["pairs"][0]["orders"][0], failed["pairs"][0]["orders"][0])

    def test_advances_actual_winner_and_report_snapshot_is_immutable(self):
        subs = [self.submission(v, t) for v in range(2) for t in range(5)]
        # Give each solution a distinct deterministic preference, with A best.
        for index, sub in enumerate(subs):
            sub["text"] = str(index % 5)
            self.app.state.store.put("submission", sub)
        def judge(scenario, answers):
            first = .9 if int(answers["answer_1"]) < int(answers["answer_2"]) else .1
            return {"answer_1": first, "answer_2": 1-first}, {}
        self.g.judge = judge
        r = self.client.post("/api/reports", json={"name": "winners", "submissions": [s["id"] for s in subs]}).json()
        result = self.wait(r["id"])
        cross = [p for p in result["pairs"] if p["stage"] == "cross"]
        self.assertEqual(len(cross), 1)
        self.assertEqual(set(cross[0]["ids"]), {subs[0]["id"], subs[5]["id"]})
        self.client.patch('/api/submissions/'+subs[0]["id"], json={"notes": "Changed", "included": False})
        self.assertEqual(self.app.state.store.get("report", r["id"])["submissions"][0]["notes"], "")

    def test_invalid_judge_values_rejected(self):
        g = Gateway()
        for probs in [{"answer_1": float("nan"), "answer_2": .5}, {"answer_1": -.2, "answer_2": 1.2}, {"answer_1": .5}]:
            g.post = lambda *args: {"answers": {"better": {"probabilities": probs}}}
            with self.assertRaises(ValueError):
                g.judge("scenario", {"answer_1": "one", "answer_2": "two"})


if __name__ == "__main__":
    unittest.main()

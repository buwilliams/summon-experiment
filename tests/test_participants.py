import tempfile
import unittest
from pathlib import Path
from fastapi.testclient import TestClient
from summon.web import create_app


class ParticipantTests(unittest.TestCase):
    def test_names_stay_with_batches_sessions_and_selected_responses(self):
        class Fake:
            def chat(self, messages):
                return {'role': 'assistant', 'content': 'Run a pilot.'}, {}
        with tempfile.TemporaryDirectory() as folder:
            client = TestClient(create_app(Path(folder), Fake()))
            batches = [client.post('/api/batches', params={'participant': name}).json()
                       for name in ['  Alex   Smith ', 'Blair']]
            for batch, name in zip(batches, ['Alex Smith', 'Blair']):
                self.assertEqual(batch['participant'], name)
                session = client.post('/api/interview/next', params={'batch_id': batch['id']}).json()
                self.assertEqual(session['participant'], name)
                submitted = client.post('/api/sessions/'+session['id']+'/submit', json={'message': 1}).json()
                self.assertEqual(submitted['participant'], name)
                revised = client.post('/api/sessions/'+session['id']+'/revise').json()
                self.assertEqual(revised['participant'], name)
            for name in ['  ', 'x'*101]:
                self.assertEqual(client.post('/api/batches', params={'participant': name}).status_code, 400)
            self.assertEqual(len(client.get('/api/batches').json()), 2)

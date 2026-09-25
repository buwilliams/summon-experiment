import copy
import unittest

from summon.studies import with_studies, study_scope


class CatalogMigrationTests(unittest.TestCase):
    def test_cases_become_experiments_without_losing_scoped_openings(self):
        old = dict(id='catalog', revision=5,
            hypotheses=[dict(id='h', name='Hypothesis', statement='Claim')],
            experiments=[dict(id='study', name='Study', hypothesis_id='h',
                             scenario_ids=['one', 'two'], view_ids=['lens'])],
            scenarios=[dict(id='one', name='First', text='First case'),
                       dict(id='two', name='Second', text='Second case')],
            views=[dict(id='lens', name='Perspective', styles=[dict(id='style', name='A',
                opening='{{SCENARIO}}\nDefault', openings={'one': '{{SCENARIO}}\nSpecific'})])])
        snapshot = copy.deepcopy(old)
        new = with_studies(old)
        self.assertEqual(old, snapshot)
        self.assertNotIn('scenarios', new)
        self.assertEqual([e['name'] for e in new['experiments']], ['First', 'Second'])
        self.assertEqual([e['text'] for e in new['experiments']], ['First case', 'Second case'])
        self.assertTrue(all(e['hypothesis_id'] == 'h' for e in new['experiments']))
        self.assertEqual(new['views'][0]['styles'][0]['openings']['one'], '{{EXPERIMENT}}\nSpecific')
        self.assertEqual(with_studies(new), new)
        scope, experiment, _ = study_scope(new, 'two')
        self.assertEqual([s['id'] for s in scope['scenarios']], ['two'])
        self.assertEqual(experiment['text'], 'Second case')

    def test_shared_case_preserves_each_hypothesis_and_its_test_scope(self):
        old = dict(id='catalog', revision=1,
            hypotheses=[dict(id=x, name=x, statement=x) for x in ['h1', 'h2']],
            experiments=[dict(id='study-'+h, name=h, hypothesis_id=h, scenario_ids=['s'], view_ids=[v])
                         for h, v in [('h1', 'v1'), ('h2', 'v2')]],
            scenarios=[dict(id='s', name='Case', text='Case text')],
            views=[dict(id=v, name=v, styles=[dict(id=v+'style', name='A', opening='Default',
                                                 openings={'s': 'Custom'})]) for v in ['v1', 'v2']])
        new = with_studies(old)
        self.assertEqual(len(new['experiments']), 2)
        self.assertEqual(new['experiments'][1]['view_ids'], ['v2'])
        second = new['experiments'][1]['id']
        self.assertEqual(new['views'][1]['styles'][0]['openings'][second], 'Custom')

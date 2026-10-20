"""Check recovery failures that must not silently resume a research window."""
import copy
import json
import os
import subprocess
import sys
import unittest
from unittest.mock import Mock, patch

import research_state


class ResearchRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(research_state.LEDGER.read_text(encoding='utf-8'))

    def test_current_state_is_valid(self):
        self.assertEqual(research_state.validate(self.data), [])

    def test_show_recovers_unicode_on_a_legacy_console(self):
        environment = dict(os.environ, PYTHONIOENCODING='ascii')
        result = subprocess.run([sys.executable, str(research_state.__file__), 'show'],
                                env=environment, capture_output=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('首问题', result.stdout)
        achieved = '是' if self.data['goal']['achieved'] else '否'
        self.assertIn(f'数值目标已实现：{achieved}', result.stdout)

    def test_changed_evidence_cannot_remain_a_live_dependency(self):
        data = copy.deepcopy(self.data)
        parent = next(claim for claim in data['claims'] if claim['id'] == 'c262_cover')
        parent.update(status='invalidated', correction='Test: metric normalization found wrong')
        self.assertTrue(any('depends on changed evidence' in error
                            for error in research_state.validate(data)))

    def test_claim_cycle_is_rejected(self):
        data = copy.deepcopy(self.data)
        first, second = data['claims'][:2]
        first['dependencies'] = [second['id']]
        second['dependencies'] = [first['id']]
        self.assertTrue(any('cycle' in error for error in research_state.validate(data)))

    def test_task_renaming_does_not_extend_an_exhausted_window(self):
        data = copy.deepcopy(self.data)
        window = research_state.current_window(data)
        window['completed_rounds'] = window['maximum_completed_rounds']
        data['current_task']['id'] = 'renamed_same_research'
        data['current_task']['round'] = window['first_round'] + window['completed_rounds']
        data['review']['last_completed_round'] = data['current_task']['round'] - 1
        self.assertTrue(any('exhausted or closed' in error
                            for error in research_state.validate(data)))

    def test_a_second_active_window_cannot_hide_the_exhausted_one(self):
        data = copy.deepcopy(self.data)
        old = research_state.current_window(data)
        old['completed_rounds'] = old['maximum_completed_rounds']
        new = dict(old, id='same_source_new_window', completed_rounds=0,
                   first_round=old['first_round'] + old['maximum_completed_rounds'])
        data['windows'].append(new)
        data['current_task'].update(window_id=new['id'], round=new['first_round'])
        errors = research_state.validate(data)
        self.assertTrue(any('Multiple active windows' in error for error in errors))
        self.assertTrue(any('Exhausted persistent window' in error for error in errors))

    def test_diagnostic_records_do_not_complete_the_numerical_goal(self):
        data = copy.deepcopy(self.data)
        data['goal'].update(achieved=True, status='complete')
        self.assertTrue(any('registered current numerical theorem' in error
                            for error in research_state.validate(data)))

    def test_invalidated_numerical_claim_cannot_complete_the_goal(self):
        data = copy.deepcopy(self.data)
        data['goal'].update(achieved=True, status='complete')
        claim = data['claims'][0]
        claim.update(type='numeric_theorem', status='invalidated',
                     correction='Test: the numerical proof was withdrawn')
        self.assertTrue(any('registered current numerical theorem' in error
                            for error in research_state.validate(data)))

    def test_stale_snapshot_fails_the_check_command(self):
        ledger, snapshot = Mock(), Mock()
        ledger.read_text.return_value = json.dumps(self.data)
        snapshot.is_file.return_value = True
        snapshot.read_text.return_value = 'Previous round: everything is still worth pursuing'
        with patch.object(research_state, 'LEDGER', ledger), \
                patch.object(research_state, 'SNAPSHOT', snapshot), \
                patch('sys.argv', ['research_state.py', 'check']):
            with self.assertRaisesRegex(SystemExit, 'Stale STATE'):
                research_state.main()

    def test_review_does_not_reset_consecutive_stagnation(self):
        for since, stagnant, due in [(1, 2, True), (0, 2, False), (1, 1, False)]:
            with self.subTest(since=since, stagnant=stagnant):
                data = copy.deepcopy(self.data)
                data['review'].update(last_global_review_round=277,
                                      last_completed_round=277 + since,
                                      rounds_without_feasibility_progress=stagnant)
                state = research_state.snapshot(data)
                self.assertIn(f'现在须复盘：{"是" if due else "否"}。', state)


if __name__ == '__main__':
    unittest.main()

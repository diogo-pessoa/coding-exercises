from unittest import TestCase

from coded_solutions.hackerRank.deployment_check.deployment_check import evaluate_deployments


class TestOrderedConfig(TestCase):

    def test_evaluate_deployments(self):
        self.assertEqual(evaluate_deployments([
            '{"deployment_id": "d-123456abcd", "status": "Success"}',
            '{"deployment_id": "d-098765efgh", "status": "Fail"}'
        ]), [1, 1, 0])

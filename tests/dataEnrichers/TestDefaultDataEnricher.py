import unittest

from dataEnrichers.DefaultDataEnricher import DefaultDataEnricher
from tests.fixtures.fixtures import CALLS, OPERATORS, CALL_SUMMARY


class MyTestCase(unittest.TestCase):

    def test_combine_data(self):
        combined_data = DefaultDataEnricher.combine_data(CALLS, OPERATORS)

        self.assertEqual(len(combined_data), 2)
        self.assertEqual(combined_data, CALL_SUMMARY)

    def test_get_prefix_range(self):
        phone_number = '+442143999888'

        self.assertEqual(DefaultDataEnricher.get_prefix_range(phone_number), 2000)

    def test_get_risk_score(self):
        call = CALLS[0]

        call.green_list = False

        # Call not in red or green list
        self.assertEqual(DefaultDataEnricher.get_risk_score(call), 0.4)

        call.red_list = True

        # Call in red list
        self.assertEqual(DefaultDataEnricher.get_risk_score(call), 1.0)

        call.red_list = False
        call.green_list = True

        # Call in green list
        self.assertEqual(DefaultDataEnricher.get_risk_score(call), 0.0)

        call.red_list = True

        # Call in green and red list
        self.assertEqual(DefaultDataEnricher.get_risk_score(call), 0.0)


if __name__ == '__main__':
    unittest.main()

import unittest

from parameterized import parameterized

from data_enrichers.DefaultDataEnricher import DefaultDataEnricher
from tests.fixtures.fixtures import CALLS, OPERATORS, CALLS_SUMMARIES


class MyTestCase(unittest.TestCase):

    def test_combine_data(self):
        combined_data = DefaultDataEnricher.combine_data(CALLS, OPERATORS)

        self.assertEqual(len(combined_data), 2)
        self.assertEqual(combined_data, CALLS_SUMMARIES)

    @parameterized.expand([
        ('+442143999888', 2000),
        ('+445943999888', 5000),
        ('Withheld', -1),
    ])
    def test_get_prefix_range(self, phone_number: str, expected_outcome: int):
        self.assertEqual(DefaultDataEnricher.get_prefix_range(phone_number), expected_outcome)

    @parameterized.expand([
        (0.42, False, False, 0.4),
        (0.45, False, False, 0.5),
        (0.42, True, False, 0.0),
        (0.42, False, True, 1.0),
        (0.42, True, True, 0.0),
    ])
    def test_get_risk_score(self, risk_sore: float, in_green_list: bool, in_red_list: bool, expected_outcome: float):
        # For some reason, running this test individually fails so when testing run the entire file
        self.assertEqual(DefaultDataEnricher.get_risk_score(
            risk_sore,
            in_green_list=in_green_list,
            in_red_list=in_red_list
        ),
            expected_outcome)


if __name__ == '__main__':
    unittest.main()

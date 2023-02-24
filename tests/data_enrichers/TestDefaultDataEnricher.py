import unittest

from data_enrichers.DefaultDataEnricher import DefaultDataEnricher
from tests.fixtures.fixtures import CALLS, OPERATORS, CALLS_SUMMARIES


class MyTestCase(unittest.TestCase):

    def test_combine_data(self):
        combined_data = DefaultDataEnricher.combine_data(CALLS, OPERATORS)

        self.assertEqual(len(combined_data), 2)
        self.assertEqual(combined_data, CALLS_SUMMARIES)

    def test_get_prefix_range(self):
        phone_number = '+442143999888'

        self.assertEqual(DefaultDataEnricher.get_prefix_range(phone_number), 2000)

        phone_number = 'Withheld'

        self.assertEqual(DefaultDataEnricher.get_prefix_range(phone_number), -1)

    def test_get_risk_score(self):
        param_list = [
            (0.42, False, False, 0.4),
            (0.45, False, False, 0.5),
            (0.42, True, False, 0.0),
            (0.42, False, True, 1.0),
            (0.42, True, True, 0.0),
        ]

        for risk_sore, in_green_list, in_red_list, expected in param_list:
            with self.subTest():
                self.assertEqual(
                    DefaultDataEnricher.get_risk_score(risk_sore,
                                                       in_green_list=in_green_list,
                                                       in_red_list=in_red_list),
                    expected)


if __name__ == '__main__':
    unittest.main()

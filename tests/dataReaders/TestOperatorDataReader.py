import unittest
from typing import Dict

from dataReaders.OperatorDataReader import OperatorDataReader
from models.Operator import Operator
from models.OperatorBuilder import OperatorBuilder


def get_expected_operators() -> Dict[int, Operator]:
    operator1 = OperatorBuilder() \
        .operator_name('Vodafone') \
        .operator_prefix(1000) \
        .operator_type('operator') \
        .operator_id('2c4fae60-cf43-4f27-869e-a9ed8b0ca25b') \
        .build()

    operator2 = OperatorBuilder() \
        .operator_name('EE') \
        .operator_prefix(2000) \
        .operator_type('operator') \
        .operator_id('8f1b1354-26d2-4e16-9582-9156a0d9a5de') \
        .build()

    return {1000: operator1, 2000: operator2}


class TestOperatorDataReader(unittest.TestCase):
    def test_read_file(self):
        expected_operators = get_expected_operators()

        operators = OperatorDataReader.read_data('../resources/operators.json')

        self.assertEqual(len(operators), 2)
        self.assertEqual(operators, expected_operators)


if __name__ == '__main__':
    unittest.main()

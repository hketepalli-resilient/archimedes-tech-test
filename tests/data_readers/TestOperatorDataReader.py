import unittest

from data_readers.OperatorDataReader import OperatorDataReader
from tests.fixtures.fixtures import OPERATORS


class TestOperatorDataReader(unittest.TestCase):
    def test_read_file(self):
        operators = OperatorDataReader.read_data('../resources/operators.json')

        self.assertEqual(len(operators), 2)
        self.assertEqual(operators, OPERATORS)


if __name__ == '__main__':
    unittest.main()

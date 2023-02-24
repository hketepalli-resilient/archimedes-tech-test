import unittest

from data_readers.CallDataReader import CallDataReader
from tests.fixtures.fixtures import CALLS


class TestCallDataReader(unittest.TestCase):
    def test_read_file(self):
        calls = CallDataReader.read_data('../resources/calls.json')

        self.assertEqual(len(calls), 2)
        self.assertEqual(calls, CALLS)


if __name__ == '__main__':
    unittest.main()

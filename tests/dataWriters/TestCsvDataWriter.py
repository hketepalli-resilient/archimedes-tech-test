import unittest

from dataWriters.CsvDataWriter import CsvDataWriter
from tests.fixtures.fixtures import CALLS_SUMMARIES


class MyTestCase(unittest.TestCase):
    def test_write(self):
        CsvDataWriter.write(CALLS_SUMMARIES)
        expected_first_data_line = '2c4fae60-cf43-4f27-869e-a9ed8b0ca25b,2020-10-12,+44123456789,Vodafone,0.0\n'

        with open('calls_summaries.txt', 'r') as f:
            for idx, line in enumerate(f):
                if idx == 1:
                    self.assertEqual(line, expected_first_data_line)

            # assert there are 3 lines in the file
            self.assertEqual(idx + 1, 3)


if __name__ == '__main__':
    unittest.main()

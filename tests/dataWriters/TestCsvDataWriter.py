import unittest

from dataWriters.CsvDataWriter import CsvDataWriter
from tests.fixtures.fixtures import CALLS_SUMMARIES


class MyTestCase(unittest.TestCase):
    def test_write(self):
        CsvDataWriter.write(CALLS_SUMMARIES)

        with open('calls_summaries.txt', 'r') as f:
            lines = 0
            for line in f:
                lines += 1

            self.assertEqual(lines, 3)

    def test_get_date(self):
        expected_string = '2c4fae60-cf43-4f27-869e-a9ed8b0ca25b,2020-10-12,+44123456789,Vodafone,0.0'

        self.assertEqual(CsvDataWriter.get_csv_string(CALLS_SUMMARIES[0]), expected_string)


if __name__ == '__main__':
    unittest.main()

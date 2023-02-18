import unittest
from datetime import datetime
from typing import List

from dataReaders.CallDataReader import CallDataReader
from models.Call import Call
from models.CallBuilder import CallBuilder

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


def get_expected_calls() -> List[Call]:
    call1 = CallBuilder().in_green_list() \
        .phone_number('+44123456789') \
        .risk_score(0.431513435443) \
        .datetime(datetime.strptime('2020-10-12T07:20:50.52Z', DATETIME_FORMAT)) \
        .call_id('2c4fae60-cf43-4f27-869e-a9ed8b0ca25b') \
        .build()

    call2 = CallBuilder().in_red_list() \
        .phone_number('+44123456789') \
        .risk_score(0.123444) \
        .datetime(datetime.strptime('2019-10-12T07:20:50.52Z', DATETIME_FORMAT)) \
        .call_id('8f1b1354-26d2-4e16-9582-9156a0d9a5de') \
        .build()

    return [call1, call2]


class TestCallDataReader(unittest.TestCase):
    def test_read_file(self):
        expected_calls = get_expected_calls()

        calls = CallDataReader.read_data('../resources/calls.json')

        self.assertEqual(len(calls), 2)
        self.assertEqual(calls, expected_calls)


if __name__ == '__main__':
    unittest.main()

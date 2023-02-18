import json
from typing import List

import iso8601

from models.Call import Call
from models.CallBuilder import CallBuilder
from .DataReader import DataReader


class CallDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> List[Call]:
        with open(filename, 'r') as f:
            data = json.load(f)
            calls = []

            for call in data['data']:
                calls.append(CallBuilder().type(call['type'])
                             .in_red_list(call['attributes'].get('redList'))
                             .in_green_list(call['attributes'].get('greenList'))
                             .phone_number(call['attributes'].get('number'))
                             .risk_score(call['attributes']['riskScore'])
                             .datetime(iso8601.parse_date(call['attributes']['date']))
                             .call_id(call['id'])
                             .build())

            return calls

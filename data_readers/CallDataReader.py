import json
from typing import List

import iso8601

from models.Call import *
from .DataReader import DataReader


class CallDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> List[Call]:
        with open(filename, 'r') as f:
            data = json.load(f)
            calls = []

            for call in data['data']:
                call_builder = CallBuilder()

                call_builder.type(call['type']) \
                    .risk_score(call['attributes']['riskScore']) \
                    .call_id(call['id']) \
                    .datetime(iso8601.parse_date(call['attributes']['date']))

                if 'redList' in call['attributes']:
                    call_builder.in_red_list(call['attributes']['redList'])

                if 'greenList' in call['attributes']:
                    call_builder.in_green_list(call['attributes']['greenList'])

                if 'number' in call['attributes']:
                    call_builder.phone_number(call['attributes']['number'])

                calls.append(call_builder.build())

            return calls

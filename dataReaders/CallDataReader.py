import json
from datetime import datetime
from typing import List

from models.Call import Call
from models.CallBuilder import CallBuilder
from .DataReader import DataReader

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class CallDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> List[Call]:
        with open(filename, 'r') as f:
            data = json.load(f)
            calls = []

            for call in data['data']:
                calls.append(CallBuilder().call_type(call['type'])
                             .in_red_list(call['attributes']['redList'])
                             .in_green_list(call['attributes']['greenList']) \
                             .phone_number(call['attributes']['number']) \
                             .call_risk_score(call['attributes']['riskScore']) \
                             .call_datetime(datetime.strptime(call['attributes']['date'], DATETIME_FORMAT)) \
                             .call_id(call['id']) \
                             .build())

            return calls

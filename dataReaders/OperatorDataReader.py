import json
from typing import Dict

from models.Operator import *
from .DataReader import DataReader


class OperatorDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> Dict[OperatorPrefix, Operator]:
        with open(filename, 'r') as f:
            data = json.load(f)
            operators = {}

            for operator in data['data']:
                prefix = int(operator['attributes']['prefix'])

                operators[prefix] = OperatorBuilder().prefix(prefix) \
                    .type(operator['type']) \
                    .operator_id(operator['id']) \
                    .name(operator['attributes']['operator']) \
                    .build()

            return operators

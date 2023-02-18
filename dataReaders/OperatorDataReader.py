import json
from typing import Dict

from models.Operator import Operator
from models.OperatorBuilder import OperatorBuilder
from .DataReader import DataReader


class OperatorDataReader(DataReader):

    # Returns a dict[operator prefix, operator]
    @staticmethod
    def read_data(filename: str) -> Dict[int, Operator]:
        with open(filename, 'r') as f:
            data = json.load(f)
            operators = {}

            for operator in data['data']:
                prefix = int(operator['attributes']['prefix'])

                operators[prefix] = OperatorBuilder() \
                    .name(operator['attributes'].get('operator') if operator['attributes'] else None) \
                    .prefix(prefix) \
                    .type(operator['type']) \
                    .operator_id(operator['id']) \
                    .build()

            return operators

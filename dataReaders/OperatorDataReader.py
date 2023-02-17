from typing import Dict

from models.Operator import Operator
from .DataReader import DataReader


class OperatorDataReader(DataReader):

    # Returns a dict[operator prefix, operator]
    @staticmethod
    def read_data(filename: str) -> Dict[str, Operator]:
        pass

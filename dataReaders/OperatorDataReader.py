from typing import Dict

from DataReader import DataReader
from models.Operator import Operator


class OperatorCallReader(DataReader):

    # Returns a dict[operator prefix, operator]
    @staticmethod
    def read_data(filename: str) -> Dict[str, Operator]:
        pass

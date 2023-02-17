from typing import List

from DataReader import DataReader
from models.Call import Call


class CallDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> List[Call]:
        pass

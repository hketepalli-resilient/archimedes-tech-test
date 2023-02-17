from typing import List

from models.Call import Call
from .DataReader import DataReader


class CallDataReader(DataReader):

    @staticmethod
    def read_data(filename: str) -> List[Call]:
        pass

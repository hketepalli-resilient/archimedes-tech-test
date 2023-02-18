from typing import List

from models.CallSummary import CallSummary
from .DataWriter import DataWriter


class CsvDataWriter(DataWriter):

    @staticmethod
    def write(data: List[CallSummary]):
        pass

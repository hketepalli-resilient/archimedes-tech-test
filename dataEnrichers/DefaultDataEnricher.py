from typing import List, Dict

from models.Call import Call
from models.CallSummary import CallSummary
from models.Operator import Operator
from .DataEnricher import DataEnricher


class DefaultDataEnricher(DataEnricher):

    @staticmethod
    def combine_data(calls: List[Call], operators: Dict[int, Operator]) -> List[CallSummary]:
        pass

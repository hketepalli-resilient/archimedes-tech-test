from abc import ABC, abstractmethod
from typing import List, Dict

from models.Call import Call
from models.CallSummary import CallSummary
from models.Operator import Operator, OperatorPrefix


class DataEnricher(ABC):

    @staticmethod
    @abstractmethod
    def combine_data(calls: List[Call], operators: Dict[OperatorPrefix, Operator]) -> List[CallSummary]:
        pass

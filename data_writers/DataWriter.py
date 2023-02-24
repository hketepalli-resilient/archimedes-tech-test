from abc import ABC, abstractmethod
from typing import List

from models.CallSummary import CallSummary


class DataWriter(ABC):

    @staticmethod
    @abstractmethod
    def write(data: List[CallSummary]):
        pass

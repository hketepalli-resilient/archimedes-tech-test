from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class DataReader(ABC):

    @staticmethod
    @abstractmethod
    def read_data(filename: str) -> T:
        pass

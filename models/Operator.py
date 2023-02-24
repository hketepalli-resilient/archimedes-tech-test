from dataclasses import dataclass

from typing_extensions import TypeAlias

OperatorPrefix: TypeAlias = int


@dataclass
class Operator:
    type: str
    id: str
    prefix: OperatorPrefix
    name: str

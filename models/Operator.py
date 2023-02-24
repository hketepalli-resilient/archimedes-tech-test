from dataclasses import dataclass

from typing_extensions import TypeAlias

OperatorPrefix: TypeAlias = int


@dataclass
class Operator:
    type: str
    id: str
    prefix: OperatorPrefix
    name: str


class OperatorBuilder:

    def __init__(self):
        self._type = 'operator'
        self._id = ''
        self._prefix = None
        self._name = ''

    def type(self, operator_type: str) -> "OperatorBuilder":
        if operator_type is not None:
            self._type = operator_type

        return self

    def operator_id(self, operator_id: str) -> "OperatorBuilder":
        self._id = operator_id
        return self

    def prefix(self, prefix: OperatorPrefix) -> "OperatorBuilder":
        self._prefix = prefix
        return self

    def name(self, name: str) -> "OperatorBuilder":
        if name is not None:
            self._name = name

        return self

    def build(self) -> Operator:
        if not self._id:
            raise Exception('Operator ID is not present')

        if not self._prefix:
            raise Exception('Operator prefix is not present')

        if not self._name:
            raise Exception('Operator name is not present')

        return Operator(self._type, self._id, self._prefix, self._name)

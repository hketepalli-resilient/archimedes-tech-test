from .Operator import Operator


class OperatorBuilder:

    def __init__(self):
        self._type = 'operator'
        self._id = ''
        self._prefix = None
        self._name = 'Unknown'

    def type(self, operator_type: str) -> "OperatorBuilder":
        if operator_type is not None:
            self._type = operator_type
            
        return self

    def operator_id(self, operator_id: str) -> "OperatorBuilder":
        self._id = operator_id
        return self

    def prefix(self, prefix: int) -> "OperatorBuilder":
        self._prefix = prefix
        return self

    def name(self, name: str) -> "OperatorBuilder":
        if name is not None:
            self._name = name

        return self

    def build(self) -> Operator:
        return Operator(self._type, self._id, self._prefix, self._name)

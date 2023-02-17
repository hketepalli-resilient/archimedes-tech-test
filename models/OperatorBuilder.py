from .Operator import Operator


class OperatorBuilder:

    def __init__(self):
        self.type = ''
        self.id = ''
        self.prefix = None
        self.name = ''

    def operator_type(self, operator_type: str) -> "OperatorBuilder":
        self.type = operator_type
        return self

    def operator_id(self, operator_id: str) -> "OperatorBuilder":
        self.id = operator_id
        return self

    def operator_prefix(self, operator_prefix: int) -> "OperatorBuilder":
        self.prefix = operator_prefix
        return self

    def operator_name(self, operator_name: str) -> "OperatorBuilder":
        self.name = operator_name
        return self

    def build(self) -> Operator:
        return Operator(self.type, self.id, self.prefix, self.name)

from typing_extensions import TypeAlias

OperatorPrefix: TypeAlias = int


class Operator:

    def __eq__(self, operator: "Operator") -> bool:
        return self.type == operator.type and \
               self.id == operator.id and \
               self.prefix == operator.prefix and \
               self.name == operator.name

    def __init__(self,
                 operator_type: str,
                 operator_id: str,
                 operator_prefix: OperatorPrefix,
                 operator_name: str):
        self.type = operator_type
        self.id = operator_id
        self.prefix = operator_prefix
        self.name = operator_name

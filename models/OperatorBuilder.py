class OperatorBuilder:

    def __init__(self):
        self.type = ''
        self.id = ''
        self.prefix = ''
        self.name = ''

    def type(self, operator_type: str) -> "OperatorBuilder":
        self.type = operator_type
        return self

    def id(self, operator_id: str) -> "OperatorBuilder":
        self.id = operator_id
        return self

    def prefix(self, operator_prefix: str) -> "OperatorBuilder":
        self.prefix = operator_prefix
        return self

    def name(self, operator_name: str) -> "OperatorBuilder":
        self.name = operator_name
        return self

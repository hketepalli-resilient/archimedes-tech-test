class Operator:

    def __eq__(self, operator: "Operator") -> bool:
        return self.type == operator.type and \
               self.id == operator.id and \
               self.prefix == operator.prefix and \
               self.name == operator.name

    def __init__(self,
                 operator_type: str,
                 operator_id: str,
                 operator_prefix: int,
                 operator_name: str):
        if operator_type:
            self.type = operator_type
        else:
            raise Exception('Operator type is not present')

        if operator_id:
            self.id = operator_id
        else:
            raise Exception('Operator ID is not present')

        if operator_prefix:
            self.prefix = operator_prefix
        else:
            raise Exception('Operator prefix is not present')

        self.name = operator_name

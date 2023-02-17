class Operator:

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

        if operator_name:
            self.name = operator_name
        else:
            raise Exception('Operator name is not present')

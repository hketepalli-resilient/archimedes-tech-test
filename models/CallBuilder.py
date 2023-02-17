from datetime import datetime

from .Call import Call


class CallBuilder:

    def __init__(self):
        self.type = 'call'
        self.id = ''
        self.datetime = datetime.now()
        self.risk_score = None
        self.number = 'Withheld'
        self.green_list = False
        self.red_list = False

    def type(self, call_type: str) -> "CallBuilder":
        self.type = call_type
        return self

    def id(self, call_id: str) -> "CallBuilder":
        self.id = call_id
        return self

    def datetime(self, call_datetime: datetime) -> "CallBuilder":
        self.datetime = call_datetime
        return self

    def risk_score(self, call_risk_score: float) -> "CallBuilder":
        self.risk_score = call_risk_score
        return self

    def number(self, phone_number: str) -> "CallBuilder":
        self.number = phone_number
        return self

    def green_list(self, in_green_list: bool = True) -> "CallBuilder":
        self.green_list = in_green_list
        return self

    def red_list(self, in_red_list: bool = True) -> "CallBuilder":
        self.red_list = in_red_list
        return self

    def build(self) -> Call:
        return Call(self.type, self.id, self.datetime, self.risk_score, self.number, self.green_list, self.red_list)

from datetime import datetime

from .Call import Call


class CallBuilder:

    def __init__(self):
        self._type = 'call'
        self._id = ''
        self._datetime = datetime.now()
        self._risk_score = None
        self._number = 'Withheld'
        self._green_list = False
        self._red_list = False

    def type(self, type: str) -> "CallBuilder":
        self._type = type
        return self

    def call_id(self, call_id: str) -> "CallBuilder":
        self._id = call_id
        return self

    def datetime(self, call_datetime: datetime) -> "CallBuilder":
        self._datetime = call_datetime
        return self

    def risk_score(self, risk_score: float) -> "CallBuilder":
        self._risk_score = risk_score
        return self

    def phone_number(self, phone_number: str) -> "CallBuilder":
        self._number = phone_number
        return self

    def in_green_list(self, in_green_list: bool = True) -> "CallBuilder":
        self._green_list = in_green_list
        return self

    def in_red_list(self, in_red_list: bool = True) -> "CallBuilder":
        self._red_list = in_red_list
        return self

    def build(self) -> Call:
        return Call(self._type, self._id, self._datetime, self._risk_score, self._number, self._green_list,
                    self._red_list)

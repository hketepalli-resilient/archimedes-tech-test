from datetime import datetime

from models.CallSummary import CallSummary


class CallSummaryBuilder:

    def __init__(self):
        self._call_id = ""
        self._datetime = datetime.now()
        self._number = "Withheld"
        self._operator = "Unknown"
        self._risk_score = None

    def call_id(self, call_id: str) -> "CallSummaryBuilder":
        self._call_id = call_id
        return self

    def datetime(self, call_datetime: datetime) -> "CallSummaryBuilder":
        self._datetime = call_datetime
        return self

    def phone_number(self, phone_number: str) -> "CallSummaryBuilder":
        self._number = phone_number
        return self

    def operator_name(self, operator_name: str) -> "CallSummaryBuilder":
        self._operator = operator_name
        return self

    def risk_score(self, risk_score: float) -> "CallSummaryBuilder":
        self._risk_score = risk_score
        return self

    def build(self, ) -> CallSummary:
        if not self._call_id:
            raise Exception('Call ID is not present')

        if self._risk_score is None:
            raise Exception('Risk sore is not present')

        return CallSummary(self._call_id, self._datetime, self._number, self._operator, self._risk_score)

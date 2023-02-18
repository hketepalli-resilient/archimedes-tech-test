from datetime import datetime

from models.CallSummary import CallSummary


class CallSummaryBuilder:

    def __init__(self):
        self.call_id = ""
        self.datetime = datetime.now()
        self.number = "Withheld"
        self.operator = "Unknown"
        self.risk_score = None

    def caller_id(self, caller_id: str) -> "CallSummaryBuilder":
        self.call_id = caller_id
        return self

    def call_datetime(self, call_datetime: datetime) -> "CallSummaryBuilder":
        self.datetime = call_datetime
        return self

    def phone_number(self, phone_number: str) -> "CallSummaryBuilder":
        self.number = phone_number
        return self

    def operator_name(self, operator_name: str) -> "CallSummaryBuilder":
        self.operator = operator_name
        return self

    def call_risk_score(self, call_risk_score: float) -> "CallSummaryBuilder":
        self.risk_score = call_risk_score
        return self

    def build(self, ) -> CallSummary:
        return CallSummary(self.call_id, self.datetime, self.number, self.operator, self.risk_score)

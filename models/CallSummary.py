import datetime


class CallSummary:

    def __init__(self,
                 call_id: str,
                 call_datetime: datetime,
                 phone_number: str,
                 operator_name: str,
                 call_risk_score: float):
        if call_id:
            self.call_id = call_id
        else:
            raise Exception('Call ID is not present')

        self.datetime = call_datetime
        self.number = phone_number
        self.operator = operator_name

        if call_risk_score:
            self.risk_score = call_risk_score
        else:
            raise Exception('Risk score is not present')

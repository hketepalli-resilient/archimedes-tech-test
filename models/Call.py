import datetime


class Call:
    def __eq__(self, call: "Call") -> bool:
        return self.type == call.type and \
               self.id == call.id and \
               self.datetime == call.datetime and \
               self.risk_score == call.risk_score and \
               self.number == call.number and \
               self.green_list == call.green_list and \
               self.red_list == call.red_list

    def __init__(self,
                 call_type: str,
                 call_id: str,
                 call_datetime: datetime,
                 call_risk_score: float,
                 phone_number: str,
                 in_green_list: bool,
                 in_red_list: bool):
        self.type = call_type

        if call_id:
            self.id = call_id
        else:
            raise Exception('Call ID is not present')

        self.datetime = call_datetime

        if call_risk_score:
            self.risk_score = call_risk_score
        else:
            raise Exception('Risk sore is not present')

        self.number = phone_number
        self.green_list = in_green_list
        self.red_list = in_red_list

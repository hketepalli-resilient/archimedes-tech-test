from typing import List, Dict

from models.Call import Call
from models.CallSummary import *
from models.Operator import Operator, OperatorPrefix
from .DataEnricher import DataEnricher


class DefaultDataEnricher(DataEnricher):

    @staticmethod
    def combine_data(calls: List[Call], operators: Dict[OperatorPrefix, Operator]) -> List[CallSummary]:
        calls_summaries = []

        for call in calls:
            call_summary_builder = CallSummaryBuilder() \
                .call_id(call.id) \
                .datetime(call.datetime) \
                .phone_number(call.number) \
                .risk_score(DefaultDataEnricher.get_risk_score(
                call.risk_score,
                in_green_list=call.green_list,
                in_red_list=call.red_list))

            prefix = DefaultDataEnricher.get_prefix_range(call.number)

            if prefix in operators:
                call_summary_builder.operator_name(operators[prefix].name)

            calls_summaries.append(call_summary_builder.build())

        return calls_summaries

    @staticmethod
    def get_prefix_range(phone_number: str) -> int:
        if phone_number == "Withheld":
            return -1

        # Assumes the phone numbers are start with +xx
        return int(phone_number[3] + '0' * 3)

    @staticmethod
    def get_risk_score(risk_score: float, in_green_list: bool, in_red_list: bool) -> float:
        if in_green_list:
            return 0.0
        elif in_red_list:
            return 1.0
        else:
            return round(risk_score, 1)

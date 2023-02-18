from typing import List, Dict

from models.Call import Call
from models.CallSummary import CallSummary
from models.CallSummaryBuilder import CallSummaryBuilder
from models.Operator import Operator
from .DataEnricher import DataEnricher


class DefaultDataEnricher(DataEnricher):

    @staticmethod
    def combine_data(calls: List[Call], operators: Dict[int, Operator]) -> List[CallSummary]:
        calls_summaries = []

        for call in calls:
            call_summary_builder = CallSummaryBuilder() \
                .call_id(call.id) \
                .datetime(call.datetime) \
                .phone_number(call.number) \
                .risk_score(DefaultDataEnricher.get_risk_score(call))

            prefix = DefaultDataEnricher.get_prefix_range(call.number) if call.number != "Withheld" else -1

            if prefix in operators:
                call_summary_builder.operator_name(operators[prefix].name)

            calls_summaries.append(call_summary_builder.build())

        return calls_summaries

    @staticmethod
    def get_prefix_range(phone_number: str) -> int:
        # Assumes the phone numbers are start with +xx
        return int(phone_number[3] + '0' * 3)

    @staticmethod
    def get_risk_score(call: Call) -> float:
        if call.green_list:
            return 0.0
        elif call.red_list:
            return 1.0
        else:
            return round(call.risk_score, 1)

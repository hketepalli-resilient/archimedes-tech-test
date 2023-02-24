import iso8601

from models.Call import CallBuilder
from models.CallSummary import CallSummaryBuilder
from models.Operator import OperatorBuilder

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

CALLS = [
    CallBuilder()
    .in_green_list()
    .phone_number('+44123456789')
    .risk_score(0.431513435443)
    .datetime(iso8601.parse_date('2020-10-12T07:20:50.52Z'))
    .call_id('2c4fae60-cf43-4f27-869e-a9ed8b0ca25b')
    .build(),
    CallBuilder()
    .in_red_list()
    .phone_number('+44123456789')
    .risk_score(0.123444)
    .datetime(iso8601.parse_date('2019-10-12T07:20:50.52Z'))
    .call_id('8f1b1354-26d2-4e16-9582-9156a0d9a5de')
    .build()
]

OPERATORS = {
    1000: OperatorBuilder()
    .name('Vodafone')
    .prefix(1000)
    .type('operator')
    .operator_id('2c4fae60-cf43-4f27-869e-a9ed8b0ca25b')
    .build(),
    2000: OperatorBuilder()
    .name('EE')
    .prefix(2000)
    .type('operator')
    .operator_id('8f1b1354-26d2-4e16-9582-9156a0d9a5de')
    .build()
}

CALLS_SUMMARIES = [
    CallSummaryBuilder()
    .call_id('2c4fae60-cf43-4f27-869e-a9ed8b0ca25b')
    .datetime(iso8601.parse_date('2020-10-12T07:20:50.52Z', DATETIME_FORMAT))
    .phone_number('+44123456789')
    .operator_name('Vodafone')
    .risk_score(0.0)
    .build(),
    CallSummaryBuilder()
    .call_id('8f1b1354-26d2-4e16-9582-9156a0d9a5de')
    .datetime(iso8601.parse_date('2019-10-12T07:20:50.52Z', DATETIME_FORMAT))
    .phone_number('+44123456789')
    .operator_name('Vodafone')
    .risk_score(1.0)
    .build()
]

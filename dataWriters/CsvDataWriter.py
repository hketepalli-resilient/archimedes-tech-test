from datetime import datetime
from typing import List

from models.CallSummary import CallSummary
from .DataWriter import DataWriter

HEADER_LINE = 'id,date,number,operator,riskScore\n'


class CsvDataWriter(DataWriter):

    @staticmethod
    def write(calls_summaries: List[CallSummary]):
        with open('calls_summaries.txt', 'w') as f:
            f.write(HEADER_LINE)

            for call_summary in calls_summaries:
                f.write(CsvDataWriter.get_csv_string(call_summary) + '\n')

    @staticmethod
    def get_csv_string(data: CallSummary):
        return f"{data.call_id},{CsvDataWriter.get_date(data.datetime)},{data.number},{data.operator},{data.risk_score}"

    @staticmethod
    def get_date(date_time: datetime):
        return date_time.strftime("%Y-%m-%d")

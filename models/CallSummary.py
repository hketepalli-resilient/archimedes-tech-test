from dataclasses import dataclass
from datetime import datetime


@dataclass
class CallSummary:
    call_id: str
    datetime: datetime
    number: str
    operator: str
    risk_score: float

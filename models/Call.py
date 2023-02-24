from dataclasses import dataclass
from datetime import datetime


@dataclass
class Call:
    type: str
    id: str
    datetime: datetime
    risk_score: float
    number: str
    green_list: bool
    red_list: bool

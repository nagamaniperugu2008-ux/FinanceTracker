import datetime
from dataclasses import dataclass


@dataclass
class Transaction: 
    amount: float
    type: str
    category: str
    date: datetime.date 
    note: str


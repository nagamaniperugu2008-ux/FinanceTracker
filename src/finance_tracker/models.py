import datetime
from dataclasses import dataclass


@dataclass
class Transaction: 
    id: int
    amount: float
    type: str
    category: str
    date: datetime.date 
    note: str
    
    

from datetime import datetime
from .execeptions import InvalidInputError
import re
from pathlib import Path
import argparse

def formatteddate(sdate):
    """Takes a date string as input and returns a date object"""
    return datetime.strptime(sdate,"%Y-%m-%d").date()

def formattedmoney(money):
    """ takes a string and returns as float amount value """
    try: 
        if float(money):
           return float(money)
    except ValueError:
        raise InvalidInputError("invalid amount value!")

def is_valid_date(date_string, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(date_string,date_format)
            return True
        except ValueError:
            return False


def get_csv_file_path():
    """
     Returns CSV file path
    """
    current_file_parent=Path(__file__).resolve().parent
    return current_file_parent/"data/data.csv"


def validate_amount(value):
    amount=float(value)
    if amount <= 0:
        raise argparse.ArgumentTypeError("Amount must be greater than zero")
    return amount

def validate_date(value):
    if not is_valid_date(value):
        raise argparse.ArgumentTypeError("Invalid date! Expected format: Year-month-day")
    return value
    

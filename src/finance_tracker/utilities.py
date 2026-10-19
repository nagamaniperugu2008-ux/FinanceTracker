from datetime import datetime
from .execeptions import InvalidInputError
import re
from pathlib import Path

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
"""
def is_valid_date(date_string, date_format="%Y-%m-%d"):
    if datetime.strptime(date_string,date_format):
        return True
    else:
        False
"""
def is_valid_date(date_string):
    """ Checks a string is a valid date format or not 
        if yes return true else false
    """
    pattern=r'^\d{2}-\d{2}-\d{4}$'
    if re.match(pattern,date_string):
        return True
    else:
        False

def get_csv_file_path():
    """
     Returns CSV file path
    """
    current_file_parent=Path(__file__).resolve().parent
    return current_file_parent/"data/data.csv"

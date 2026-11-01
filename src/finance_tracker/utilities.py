from datetime import datetime
from .execeptions import InvalidInputError
import re
from pathlib import Path
import argparse
import csv

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
    
def id_generate():
    """TODO:
     1. check is there any transactions if not create first transaction id
     2. or else  get the max id from the csv file 
     3. increment the max id and return a new id 
    """
    path=get_csv_file_path()
    avail_ids=[]
    next_id=None
    if not path.is_file():
        next_id=1
    else:
        with open(path,mode='r',newline='') as file:
            if path.stat().st_size==0:
                next_id=1
            else:
                try:
                    reader=csv.DictReader(file)
                    first_row=next(reader,None)
                    if first_row is None:
                        next_id=1
                    else:
                        avail_ids.append(int(first_row['id']))
                        for row in reader: 
                            if int(row['id'])<=0:
                                raise ValueError(f"invalid transaction negative ID found in csv file")   
                            avail_ids.append(int(row['id']))
                        if avail_ids:
                            next_id=max(avail_ids)+1
                except ValueError as e:
                    raise ValueError(f"invalid transaction ID found in CSV file:{e}")
    return next_id


def to_transaction_dic(dic):
    return{
            "id":int(dic['id']),
            "amount":formattedmoney(dic["amount"]),
            "type":dic["type"],
            "date":formatteddate(dic["date"]),
            "category":dic["category"],
            "note":dic["note"]            
        }

def validate_id(transaction_id):
    try:
        transaction_id=int(transaction_id)
        if not isinstance(transaction_id,int) or not transaction_id>0 :
            raise argparse.ArgumentTypeError("Invalid ID! ID must be a Positive Number")
    except ValueError:
        raise argparse.ArgumentError("Invalid ID! ID must be a Positive Number")
    return transaction_id
    

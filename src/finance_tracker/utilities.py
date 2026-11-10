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


def is_valid_amount(amount):
    if amount>0:
        return True
    else:
        return False

def validate_amount(value):
    try:
        amount=float(value)
        if not is_valid_amount(amount):
            raise argparse.ArgumentTypeError("Amount must be greater than zero")
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid amount value! amount must be a positive number")
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
                            next_id=max(avail_ids)+1  #raises value error when id is not a integer
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


def is_valid_id(transaction_id):
    if isinstance(transaction_id,int) and transaction_id>0 :
        return True
    return False

def id_exists(transaction_id):
    """
    Checks is exists or not if id exists return True
    If file doesn't exist return false
    """
    path=get_csv_file_path()
    avail_ids=[]
    if not path.is_file():
        return False
    with open(path,mode='r',newline='') as file:
        if path.stat().st_size==0:
            return False
        else :
            reader=csv.DictReader(file)
            first_row=next(reader,None)
            if first_row is None:
                return False
            else:
                avail_ids.append(int(first_row['id']))
                for row in reader: 
                    if int(row['id'])>=0:   
                        avail_ids.append(int(row['id']))
                if avail_ids:
                    if transaction_id in avail_ids:
                        return True
                    else:
                        return False

def validate_id(transaction_id):
    try:
        if is_valid_id(int(transaction_id)):
            return int(transaction_id)
    except ValueError :
        raise argparse.ArgumentTypeError("Invalid ID! ID must be a Positive Number")
    raise argparse.ArgumentTypeError("Invalid ID! ID must be a Positive Number")

def validate_attributes(test_attr):
    source={"amount","type","category","note","date"}
    if not test_attr:
        raise InvalidInputError("Invalid test_attr input")
    if test_attr.keys()<=source:
       return True
    else:
        return False
import argparse
from .utilities import validate_amount,validate_date
from .transaction_manager import *
ts=TransactionManager()
parser=argparse.ArgumentParser(description="FINANCE TRACKER")
subparsers=parser.add_subparsers(dest="command")
list_parser=subparsers.add_parser("list")
add_parser=subparsers.add_parser("add",help="add command to save transaction requird arguments amount,type,category,date note")
add_parser.add_argument("--amount",type=validate_amount,required=True)
add_parser.add_argument("--type",type=str,choices=['income','expense'],required=True)
add_parser.add_argument("--category",type=str,required=True)
add_parser.add_argument("--date",required=True,type=validate_date)
add_parser.add_argument("--note",type=str,default=None)
args=parser.parse_args()
if (args.command=="list"):
    data=ts.view()
    print(data)

if (args.command=="add"):
    dic=ts.to_transaction_dic({"amount":args.amount,"type":args.type,"category":args.category,"date":args.date,"note":args.note})
    obj=ts.create_transaction_obj(dic)
    message=ts.save_transaction_obj(obj)
    print(message)
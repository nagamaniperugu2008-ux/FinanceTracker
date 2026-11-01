import argparse
from .utilities import *
from .transaction_manager import *
ts=TransactionManager()
parser=argparse.ArgumentParser(description="FINANCE TRACKER")
subparsers=parser.add_subparsers(dest="command")
list_parser=subparsers.add_parser("list",help="for view all transactions")
add_parser=subparsers.add_parser("add",help="for to save transaction requird arguments amount,type,category,date note")
add_parser.add_argument("--amount",type=validate_amount,required=True)
add_parser.add_argument("--type",type=str,choices=['income','expense'],required=True)
add_parser.add_argument("--category",type=str,required=True)
add_parser.add_argument("--date",required=True,type=validate_date)
add_parser.add_argument("--note",type=str,default=None)
delete_parser=subparsers.add_parser("delete",help="for to delete transaction")
delete_parser.add_argument("--id",required=True,type=validate_id)
args=parser.parse_args()
if (args.command=="list"):
    data=ts.view()
    print(data)

if (args.command=="add"):
    dic=ts.create_transaction_dic({"amount":args.amount,"type":args.type,"category":args.category,"date":args.date,"note":args.note})
    obj=ts.create_transaction_obj(dic)
    message=ts.save_transaction_obj(obj)
    print(message)

if (args.command=="delete"):
    msg=ts.delete(args.id)
    print(msg)
import argparse
from .utilities import *
from .transaction_manager import *
tm=TransactionManager()
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
filter_parser=subparsers.add_parser("filter")
filter_parser.add_argument("--min",type=validate_amount)
filter_parser.add_argument("--max",type=validate_amount)
filter_parser.add_argument("--amount",type=validate_amount)
filter_parser.add_argument("--fromdate",type=validate_date)
filter_parser.add_argument("--todate",type=validate_date)
filter_parser.add_argument("--date",type=validate_date)
filter_parser.add_argument("--type",type=str,choices=['income','expense'])
filter_parser.add_argument('--category',type=str)
args=parser.parse_args()
if (args.command=="list"):
    data=tm.view()
    print(data)

if (args.command=="add"):
    dic=tm.create_transaction_dic({"amount":args.amount,"type":args.type,"category":args.category,"date":args.date,"note":args.note})
    obj=tm.create_transaction_obj(dic)
    message=tm.save_transaction_obj(obj)
    print(message)

if (args.command=="delete"):
    msg=tm.delete(args.id)
    print(msg)

if (args.command=="filter"):
    attributes={}
    if(args.date):
        attributes["date"]=args.date

    if(args.amount is not None):    
        attributes["amount"]=args.amount

    if(args.type):
        attributes["type"]=args.type

    if(args.category):
        attributes["category"]=args.category

    ts=tm.filter(attributes=attributes,fromdate=args.fromdate,todate=args.todate,min_amount=args.min,max_amount=args.max)
    print(ts) 
    
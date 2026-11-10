from .execeptions import InvalidInputError,KeyValueError
from .models import Transaction
import csv
import dataclasses
from pathlib import Path
from .utilities import *


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def create_transaction_dic(self,dic):
            return{
            "id":id_generate(),
            "amount":formattedmoney(dic["amount"]),
            "type":dic["type"],
            "date":formatteddate(dic["date"]),
            "category":dic["category"],
            "note":dic["note"]            
            }

    def create_transaction_obj(self, transaction_dict):
        """
            Takes transaction as dict,
            Returns `Transaction` object.

            Raises:
                InvalidInputError: if the dict is invalid.
        """
        # Validating dict
        if not transaction_dict or not isinstance(transaction_dict, dict):
            raise InvalidInputError("Invalid dict for create_transaction_object().")
        
        obj = Transaction(
                id=transaction_dict['id'],
                amount=transaction_dict['amount'],
                type=transaction_dict['type'],
                date=transaction_dict['date'],
                category=transaction_dict['category'],
                note=transaction_dict['note']
            )
            
        return obj


    def save_transaction_obj(self,transaction_obj):
        """ takes transaction as an object ,
            save it in csv file
        """
        #validating object

        
        if not transaction_obj or not isinstance(transaction_obj, Transaction):
            raise InvalidInputError("Invalid object for save_transaction_obj().")

        dic = dataclasses.asdict(transaction_obj) 
        
        fields=[]
        for key in dic.keys():
            fields.append(key)
        # creating csv_file_path
        
        csv_file_path=get_csv_file_path()
        
        # Automatically create the 'data' directory if it doesn't exist
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(csv_file_path,mode="a",newline="") as file:
            writer=csv.DictWriter(file, fieldnames=fields)
            if csv_file_path.stat().st_size == 0 :
                writer.writeheader()
            writer.writerow(dic)
            message="transaction saved.."
        return message

    
    def view(self):
        """
            Reads the data from csv data file.
            Returns data in the form of ________ ( we'll decide later )
        """
        # TODO:
        # 1.data extract from csv file
        csv_file_path=get_csv_file_path()
        data=[]
        if not csv_file_path.is_file():
            data="no transactions here! Create your first transaction.."
        else:
            with open(csv_file_path,mode='r',newline='')  as file:
                if csv_file_path.stat().st_size==0:
                    data="no transactions here!"
                else:
                    reader=csv.DictReader(file)
                # formatting the dictionaries  
                    for row in reader:
                        data.append(to_transaction_dic(row))
                    if not data:
                        data="no transactions here!"
        return data


        
    def delete(self,transaction_id:int):
        """
          Deletes the given transaction from the csv data file.
          Returns result of the process(deleted or not).

          Raises:
               InvalidInputError: if the dict is Invalid.
        
        """
        if not transaction_id or validate_id(transaction_id):
            raise InvalidInputError("invalid ID  to delete the transaction") 
        # extracting csv file data
        csv_file_path=get_csv_file_path()
        msg=""
        data=[]
        try:
            with open(csv_file_path,mode="r",newline='') as file:
                if csv_file_path.stat().st_size==0:
                    msg="No transactions Found!"
                else:
                    reader=csv.DictReader(file)
                # formatting the dictionaries  
                    for row in reader:
                        data.append(to_transaction_dic(row))
                    if not data:  
                        msg="No transactions Found!"
        except FileNotFoundError:
            msg="No transactions Found!"
        #checking given transaction with the data and delete
        if msg!="No transactions Found!":
            for i in data:
                if (transaction_id==i['id']):
                    confirm=input("confirm to delete the transaction y/n:")
                    if confirm=='y':
                        data.remove(i)
                        msg="deleted"
                    else:
                        return "Transaction not Deleted" 
                if msg=="deleted":
                # rewriting the data to csv file
                    fields=[]
                    for key in data[0].keys():
                        fields.append(key)
                    with open(csv_file_path,mode="w",newline="") as file:
                        writer=csv.DictWriter(file,fieldnames=fields)
                        writer.writeheader()
                        writer.writerows(data)
                else:
                    msg="Transaction is not Found!"
        #returning the result message
        return msg
        

    def filter(self, attributes=None,fromdate=None,todate=None,min_amount:float|None=None,max_amount:float|None=None):
        """
           Filter data by attributes(type,amount,date,category)
           Returns filtered data as list

           Raises:
                 InvalidInputError:if given attribute values types are invalid
        
        """
        csv_file_path=get_csv_file_path()
        try:
            with open(csv_file_path,mode="r",newline='') as file:
                    #checking file is empty or not
                    if csv_file_path.stat().st_size==0:
                        filtered_data="file is empty"
                        return
                    else:
                        # reading the file contents as dict
                        reader=csv.DictReader(file)
                        data=[]
                        #converting csv dic to transaction dic
                        for row in reader:
                            data.append(to_transaction_dic(row))
                        if not data:
                            filtered_data="No transactions available to display."
                        else:
                            filtered_data=data
        except FileNotFoundError:
            filtered_data="No transaction records found. Add a transaction first"
      
        if fromdate:
            if not is_valid_date(fromdate):
                raise InvalidInputError("Invalid date format [from date]!")
            fromdate=formatteddate(fromdate)

        if todate:
            if not is_valid_date(todate):
                raise InvalidInputError("Invalid date format [to date]!")
            todate=formatteddate(todate)
        if min_amount:
            min_amount=formattedmoney(min_amount)

        if max_amount:
            max_amount=formattedmoney(max_amount)

        if attributes:
            if "amount" in attributes:
                attributes["amount"]=formattedmoney(attributes["amount"])
            if "date" in attributes:
                attributes["date"]=formatteddate(attributes["date"])
            filtered_data=[ i for i in data 
                       if all(i.get(crit_key)==crit_val for crit_key,crit_val in attributes.items())]
        
        if fromdate or todate:
            if fromdate and todate:
                mod_data=[]
                for i in filtered_data:
                    if ((fromdate<=i["date"])and(i["date"]<=todate)):
                        mod_data.append(i)
                filtered_data=mod_data
            elif fromdate:
                mod_data=[]
                for i in filtered_data:
                    if (fromdate<=i["date"]):
                        mod_data.append(i)
                filtered_data=mod_data
            else:
                mod_data=[]
                for i in filtered_data:
                    if (todate>=i["date"]):
                        mod_data.append(i)
                filtered_data=mod_data
        if min_amount:
            mod_data=[]
            for i in filtered_data:
                if (min_amount<=i["amount"]):
                   mod_data.append(i)
            filtered_data=mod_data

        if max_amount:
            mod_data=[]

            for i in filtered_data:
                if (max_amount>=i["amount"]):
                    mod_data.append(i)
            filtered_data=mod_data

        if not filtered_data:
            filtered_data="No transactions found matching the given filters"
        
        return filtered_data

    
    def edit(self,transaction_id,attributes):
        """
           Edit the existed transaction.
           takes input id and attribute and date to change(type="expense").
           Returns message updated or not. 

        """
        if not validate_id(transaction_id):
            raise InvalidInputError("Invalid Transaction_id to edit! Transaction_id must be a Positive number")
        if not isinstance(attributes,dict):
            raise InvalidInputError("Invalid attribute type! it takes dictionary value")
        if  not validate_attributes(attributes) :
            raise InvalidInputError("Invalid attribute! Allowed attributes: amount,type,category,date,note")
        csvfile_path=get_csv_file_path()
        if csvfile_path.is_file():
            if id_exists(transaction_id):
                msg=""
                data=[]
                flag=0
                if "amount" in attributes:
                    if is_valid_amount(attributes["amount"]):
                        attributes["amount"]=formattedmoney(attributes["amount"])
                    else:
                        raise InvalidInputError("Invalid amount! amount must be positive number")
                if "date" in attributes:
                    if is_valid_date(attributes["date"]):
                        attributes["date"]=formatteddate(attributes['date'])
                    else:
                        raise InvalidInputError("Invalid date! date must be in the form %y%m%d")
                if "type" in attributes:
                    if not attributes["type"] in ["income","expense"]:
                        raise InvalidInputError("Invalid Type! takes only income or expense ")
                with open(csvfile_path,mode='r',newline="") as file:
                        reader=csv.DictReader(file)
                        #formatting the dictionaries
                        for row in reader:
                            data.append(to_transaction_dic(row))
                for i,row in enumerate(data):
                        if row['id']==transaction_id:
                            for key,value in attributes.items():
                                data[i][key]=value
                            flag=1
                if flag==1:
                        fields=[]
                        for key in data[0].keys():
                            fields.append(key)
                        with open(csvfile_path,mode="w",newline='') as file:
                            writer=csv.DictWriter(file,fieldnames=fields)
                            writer.writeheader()
                            writer.writerows(data)
                        msg="Transaction Updated..."
                else:
                    msg="Transaction Not Found!"
                return msg
            else:
                 return "Transaction Not Fount!" 
        else:
            return "No transactions Found!" 
                
                


                                    

                                
                                        
from .execeptions import InvalidInputError 
from .models import Transaction
import csv
import dataclasses
from pathlib import Path


class TransactionManager:
    def __init__(self):
        self.transactions = []


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
        current_file_parent = Path(__file__).resolve().parent
        
        csv_file_path=current_file_parent/"data/data.csv"
        
        # Automatically create the 'data' directory if it doesn't exist
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(csv_file_path,mode="a",newline="") as file:
            writer=csv.DictWriter(file, fieldnames=fields)
            if csv_file_path.stat().st_size == 0 :
                writer.writeheader()
            writer.writerow(dic)
        return csv_file_path
# suuper question...
# data.csv loo emaina data undhaa, chuudu

    
    def view(self):
        """
            Reads the data from csv data file.
            Returns data in the form of ________ ( we'll decide later )
        """
        # TODO:
        # 1.data extract from csv file
        current_file_parent=Path(__file__).resolve().parent
        csv_file_path=current_file_parent/"data/data.csv"
        with open(csv_file_path,mode='r',newline='')  as file:
            if csv_file_path.stat().st_size==0:
                data="no transactions here!"
            else:
                reader=csv.DictReader(file)
                data=list(reader)
                if not data:
                    data="no transactions here!"
        return data


        
    def delete(self,transaction_dict):
        """
          Deletes the given transaction from the csv data file.
          Returns result of the process(deleted or not).

          Raises:
               InvalidInputError: if the dict is Invalid.
        
        """
        if not transaction_dict or not isinstance(transaction_dict,dict):
            raise InvalidInputError("Inavlid dict! to DeleteTransaction().")
        # extracting csv file data
        current_file_parent=Path(__file__).resolve().parent
        csv_file_path=current_file_parent/"data/data.csv"
        msg=""
        with open(csv_file_path,mode="r",newline='') as file:
            if csv_file_path.stat().st_size==0:
                msg="no transactions here!"
            else:
                reader=csv.DictReader(file)
                data=list(reader)
                if not data:
                    msg="no transactions here!"
        #checking given transaction with the data and delete
        if msg!="no transactions here!":
            for i in data:
                if (i==transaction_dict):
                    data.remove(i)
                    msg="deleted"
            if msg=="deleted":
                # rewriting the data to csv file
                fields=[]
                for key in transaction_dict.keys():
                    fields.append(key)
                with open(csv_file_path,mode="w",newline="") as file:
                     writer=csv.DictWriter(file,fieldnames=fields)
                     if csv_file_path.stat().st_size == 0 :
                        writer.writeheader()
                     writer.writerows(data)
            else:
                msg="transaction is not present!"
        #returning the result message
        return msg
        

    def filter(self, category):
        pass

    
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
        else:
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
        
        with open(csv_file_path,mode="w",newline="") as file:
            writer=csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerow(dic)

        return csv_file_path

    
    def view(self):
        pass 


    def delete(self):
        """deletes a transactions from list of transactions"""


    def filter(self, category):
        pass

    
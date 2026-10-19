from .execeptions import InvalidInputError 
from .models import Transaction
import csv
import dataclasses
from pathlib import Path
from .utilities import formatteddate,formattedmoney,is_valid_date,get_csv_file_path


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def to_transaction_dic(self,dic):
        return{
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
        print(dic)
        
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
        return csv_file_path

    
    def view(self):
        """
            Reads the data from csv data file.
            Returns data in the form of ________ ( we'll decide later )
        """
        # TODO:
        # 1.data extract from csv file
        csv_file_path=get_csv_file_path()
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
        csv_file_path=get_csv_file_path()
        msg=""
        data=[]
        with open(csv_file_path,mode="r",newline='') as file:
            if csv_file_path.stat().st_size==0:
                msg="no transactions here!"
            else:
                reader=csv.DictReader(file)
                # formatting the dictionaries  
                for row in reader:
                    data.append(self.to_transaction_dic(row))
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
        

    def filter(self, attributes=None,fromdate=None,todate=None,min_amount:float|None=None,max_amount:float|None=None):
        """
           Filter data by attributes(type,amount,date,category)
           Returns filtered data as list

           Raises:
                 InvalidInputError:if given attribute values types are invalid
        
        """
        csv_file_path=get_csv_file_path()
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
                            data.append(self.to_transaction_dic(row))
                        if not data:
                            filtered_data="file is empty"
                            return
        filtered_data=data
        if fromdate:
            if not is_valid_date(fromdate):
                raise InvalidInputError("Invalid date format fromdate!")
            fromdate=formatteddate(fromdate)

        if todate:
            if not is_valid_date(todate):
                raise InvalidInputError("Invalid date format todate!")
            todate=formatteddate(todate)
        if min_amount:
            min_amount=formattedmoney("min_money")

        if max_amount:
            max_amount=formattedmoney("max_money")

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

        
        return filtered_data

    



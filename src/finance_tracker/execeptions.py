# Exception heirarchy

# FinanceTrackerError
# |- AddTransactionError
# |  |- InvalidInputError 
# |  |- ...
# |- 


class FinanceTrackerError(Exception):
    pass

class AddTransactionError(FinanceTrackerError):
    pass

class InvalidInputError(AddTransactionError):
    pass

# import AddTransactionError into transaction_manager.py file!

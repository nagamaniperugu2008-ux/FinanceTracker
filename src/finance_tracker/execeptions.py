# Exception heirarchy

# FinanceTrackerError
# |- ATransactionError
# |  |- InvalidInputError 
# |  |- ...
# |- 
# import CreateTransactionError into transaction_manager.py file!

class FinanceTrackerError(Exception):
    pass

class CreateTransactionError(FinanceTrackerError):
    pass


class DeleteTransactionError(FinanceTrackerError):
    pass

class FilterTransactionError(FinanceTrackerError):
    pass

class InvalidInputError(CreateTransactionError,DeleteTransactionError):
    pass

class KeyValueError(CreateTransactionError,DeleteTransactionError):
    pass
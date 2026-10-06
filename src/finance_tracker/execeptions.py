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

class InavalidInputError(CreateTransactionError,DeleteTransactionError):
    pass
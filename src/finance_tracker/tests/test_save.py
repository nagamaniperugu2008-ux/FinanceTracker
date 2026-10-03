from finance_tracker.transaction_manager import TransactionManager
from datetime import date

tm = TransactionManager()

transaction = tm.create_transaction_obj({
    "amount": 300.00,
    "type": "expense",
    "category": "food",
    "date": date.today(),
    "note": "thintunna... "
})

tm.save_transaction_obj(transaction)

print("TEST OUTPUT: ",len(tm.view()))

# oyee em avthundhiii..!!! XXX???
#who knoww? u have to know..
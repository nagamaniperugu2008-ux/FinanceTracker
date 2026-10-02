from finance_tracker.transaction_manager import TransactionManager
from datetime import date


tm = TransactionManager()

# test 1
dic = {
    "amount": 500.00,
    "type": "expense",
    "category": "personal",
    "date": date.today(),
    "note": "soo rough today..."
}
obj=tm.create_transaction_obj(dic)
print("TEST1:", obj)

# test 2

print("TEST2:",tm.save_transaction_obj(obj))


# test 3

print(tm.save_transaction_obj(None))

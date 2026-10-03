from finance_tracker.transaction_manager import TransactionManager
from datetime import date


tm = TransactionManager()

# test 1
dic = {
    "amount": 200.00,
    "type": "expense",
    "category": "work",
    "date": date.today(),
    "note": "completed one module..."
}

big_dick = {
    "amount": 20.00,
    "type": "expense",
    "category": "food",
    "date": date.today(),
    "note": "icecream for bucchii"
}

obj=tm.create_transaction_obj(dic)
print("TEST1:", obj)

# test 2

print("TEST2:",tm.save_transaction_obj(obj))


# test 3

# print("TEST3:", tm.save_transaction_obj(None)) 


# test 4

print("TEST4:", tm.view())
    
# fix aindhi...!
#hi ammai

# neeku oka important skill gurinchii cheptha, ready aa...
# ee skill ey oka GOOD programmer nii, GREAT programmer ni differentiate chesthadhi...
# okk

# come come

# 
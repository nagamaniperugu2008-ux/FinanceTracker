from finance_tracker.transaction_manager import TransactionManager
from datetime import date
from ..utilities import formatteddate
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

#obj=tm.create_transaction_obj(big_dick)
#print("TEST1:", obj)

# test 2

#print("TEST2:",tm.save_transaction_obj(obj))

# test 3

#
# print("TEST3:", tm.save_transaction_obj(None)) 


# test 4

#print("TEST4:", tm.view())
    
 #print("test5:",tm.delete({"amount":300.0,"type":"expense","category":"food","date":2026-10-4}))


#print("test6:",tm.filter({"type":"expense"}))
#print("test6:",tm.filter({"category":"food"}))
#print("test6:",tm.filter({"type":"income"}))
#print("test6:",tm.filter({"category":"food"}))
print("test 7:")
for i in (tm.filter(min_amount="cjcjbhc")):
    print(i)
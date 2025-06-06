# Task: Estimate weekly and daily food expenditure based on cafeteria visits, 
# lunch price, and grocery costs
cafe=int(input("How many times a week do you eat at the student cafeteria?"))
price=float(input("The price of a typucal student lunch?"))
groceries=float(input("How much money do you spend on groceries in a week?"))
mul=groceries + cafe* price

print("Average food expenditure:")
print(f"Daily: {mul / 7} euros")
print(f"Weekly: {mul} euros")

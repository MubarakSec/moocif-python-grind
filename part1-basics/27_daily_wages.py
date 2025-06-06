# Task: Calculate daily wages from hourly wage,
# hours worked, and day; double wage if Sunday
wage=float(input("wage?"))
work=int(input("worked?"))
day=input("what day?")

if day == "Sunday":
    print(f"Daily wages: {(wage*work)*2} euros")
else:
    print(f"Daily wages: {(wage*work)} euros")

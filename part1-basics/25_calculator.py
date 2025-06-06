# Task: Ask for two numbers and an operation 
# (add, subtract, multiply),
#  perform operation and print result; else print nothing
num1=int(input("number?"))
num2=int(input("number2"))
opration=input("operation:")

if opration == "add":
    print(f"{num1} + {num2} = {num1+num2}")
if opration == "multiply":
    print(f"{num1} * {num2} = {num1*num2}")
if opration == "subtract":
    print(f"{num1} - {num2} = {num1-num2}")

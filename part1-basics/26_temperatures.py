# Task: Convert Fahrenheit to Celsius, print result; 
# if below 0°C, print a cold warning message
temperature=int(input("temperature today?"))

print(f"{temperature} degrees Fahrenheit equals {(temperature-32) /1.8} degrees Celsius")
if ((temperature-32) /1.8) < 0:
    print("Brr! It's cold in here!")

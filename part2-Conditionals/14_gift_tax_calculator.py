# Calculates Finnish gift tax for gifts ≥ €5,000 from close relatives.
# Tax = base amount + percentage on amount over thresholds.

gift= float(input("the value of the gift"))
tax=0

if gift < 5000:
    print("No tax!")
elif 5000 < gift <= 25000:
    tax = (100 + (gift - 5000) * 0.08)
elif 25000 < gift <= 55000:
    tax = (1700 + (gift - 25000) * 0.1)
elif 55000 < gift <= 200000:
    tax = (4700 + (gift - 55000) * 0.12)
elif 200000 < gift <= 1000000:
    tax = (22100 + (gift - 200000) * 0.15)
else:
    tax = (142100 + (gift - 1000000) * 0.17)
if tax > 0:
    print(f"Amount of tax: {tax} euros")

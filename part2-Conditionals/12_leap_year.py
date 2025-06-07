# Input year  
# Check leap year rules: divisible by 4,  
# except divisible by 100 unless also by 400  
# Print if leap year or not  

number = int(input("Please type in a number: "))

if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0):
    # Leap year if divisible by 4 but not 100, or divisible by 400
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

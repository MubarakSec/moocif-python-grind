# Input integer  
# Print "FizzBuzz" if divisible by 3 & 5  
# Print "Fizz" if divisible by 3  
# Print "Buzz" if divisible by 5  
 


num= int(input("number"))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 :
    print("Fizz")

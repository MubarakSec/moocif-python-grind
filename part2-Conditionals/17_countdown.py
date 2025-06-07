# Fix the code

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number <= 0: # Here was the error
    break

print("Now!")

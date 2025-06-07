# Keep asking for PIN until correct (4321), 
# then print number of attempts.

attempt=0
while True:
    pin=input("Pin:")
    attempt += 1
    if pin == "4321":
        if attempt > 1:
            print(f"Correct! It took you {attempt} attempts")
            break
        else:
            print("Correct! It only took you one single attempt!")
            break
    print("Wrong")

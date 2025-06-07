# Ask for a password, 
# then keep asking to retype until it matches the first.

password=input("password")
while True:
    secretpass=input("Repeat password:")
    if password == secretpass:
        print("User account created!")
        break
    print("They do not match!")
       
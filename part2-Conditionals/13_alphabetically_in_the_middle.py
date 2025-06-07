# Ask for three letters
# Sort the letters alphabetically
# Print the middle one

first1=input("Enter a lettter")
first2=input("Enter a lettter")
first3=input("Enter a lettter")


if first1 > first2 and first1 > first3:

    if first2 > first3:
        print("The letter in the middle is", first2)
    else:
        print("The letter in the middle is", first3)
elif first2 > first1 and first2 > first3:

    if first1 > first3:
        print("The letter in the middle is", first1)
    else:
        print("The letter in the middle is", first3)
elif first3 > first2 and first3 > first1:
    if first1 > first2:
        print("The letter in the middle is", first1)
    else:
        print("The letter in the middle is", first2)

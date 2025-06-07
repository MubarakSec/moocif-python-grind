# Ask for points received  
# Print grade based on the university course 
# grade boundaries  

grade=int(input("grade?"))
if grade > 100:
    print("Grade: impossible!")
elif 90 <= grade <=100:
    print(f"Grade: 5")
elif 80 <= grade <90:
    print(f"Grade: 4")
elif 70 <= grade <80:
    print(f"Grade: 3")
elif 60 <= grade <=70:
    print(f"Grade: 2")
elif 50 <= grade <=60:
    print(f"Grade: 1")
elif 0 < grade <=50:
    print(f"Grade: fail")
elif grade < 0:
    print("Grade: impossible!")

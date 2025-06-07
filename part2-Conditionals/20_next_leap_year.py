# Ask for a year and print the next leap year after it.

year=int(input("enter a year: "))
leap= year +1
while True:
    if leap % 400 == 0 or (leap % 4 == 0 and leap % 100 != 0):
        print(f"The next leap year after {year} is {leap}")
        break
    leap += 1

# Ask the user for two numbers
# If one is greater, print that number
# If they are equal, print a message saying so



goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The greater number was:", goals_home)
elif goals_away > goals_home:
    print("The greater number was:", goals_away)
else:
    print("The numbers are equal!")

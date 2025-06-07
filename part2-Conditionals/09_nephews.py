# Get user's name  
# If name is Huey, Dewey, or Louie, identify as Donald Duck's nephew  
# If name is Morty or Ferdie, identify as Mickey Mouse's nephew  

name=input("your name")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

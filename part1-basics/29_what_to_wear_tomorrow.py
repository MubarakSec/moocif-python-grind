# Task: Suggest clothing based on tomorrow's temperature
#  and rain forecast with escalating advice

print("What is the weather forecast for tomorrow?")
temperature=int(input("temp"))
rain=input("will it rain")


if temperature > 20:
    print("Wear jeans and a T-shirt")
elif temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

else:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

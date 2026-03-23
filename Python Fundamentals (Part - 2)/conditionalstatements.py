age = int(input("Enter your age: "))

if(age >= 18):
    print("You are eligible to vote")
    print("You can drive")
else:
    print("You are not eligible to vote")

color = str(input("Enter a colour: "))
if(color == "red"):
    print("Ohh yeah")
elif(color == "green"):
    print("Go on")
elif(color == "yellow"):
    print("Amazing")
else:
    print("Invalid color")

number = int(input("Enter a number: "))

if(number % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")
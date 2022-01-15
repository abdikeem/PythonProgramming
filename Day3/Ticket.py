print("Welcome to the rollercoaster! ")
height = int(input("What is your hieght in cm? "))
if height >= 120:
    print("You can ride a rollercoaster!")

    age = int(input("What is you Age? "))
    if age >= 18:
        print("Your ticket payment is $12 ")
    else:
        print("Your ticket payment is $7 ")
else:
    print("Ops! You can't ride on a rollercoaster") 
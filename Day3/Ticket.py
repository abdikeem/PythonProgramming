from functools import total_ordering


print("Welcome to the rollercoaster! ")
height = int(input("What is your hieght in cm? "))
adult_ticket = 12
children_ticket = 5
youth_ticket = 7
photography = 3
bill = 0
if height >= 120:
    print("You can ride a rollercoaster!")

    age = int(input("What is you Age? "))
    if age <= 12:
        bill = 5
        print(f"Child ticket payment is ${children_ticket} ")
    elif age <= 23:
        bill = 7
        print(f"Youth ticket payment is ${youth_ticket}")
    else:
        bill = 12
        print(f"Adult ticket payment is ${adult_ticket} ")
    photo = input("You want to take images? Y Or N? ")
    if photo == "y":
        bill += 3
        print(f"You will be charged ${photography} extra! Enjoy your day")
    print(f"your total bill is ${bill}")
else:
    print("Ops! You can't ride on a rollercoaster") 
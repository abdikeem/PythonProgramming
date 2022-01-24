import random 

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

print(names)

num_items = len(names)
random_names = random.randint(0, num_items - 1)

person_to_pay = names[random_names]

print("\U0001F923 " +person_to_pay + " is going to pay the bill")
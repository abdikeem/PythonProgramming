print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip = bill * tip_as_percentage
total_bill = tip + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2) #Rounded the result to 2 decimal place

print(f"Each person should pay: $ {final_amount}")
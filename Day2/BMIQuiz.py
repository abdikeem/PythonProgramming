print("Welcome to BMI interpretor:")
height = float(input("What is your height in Metres?: "))
weight = float(input("What is your Weight in Kilograms?: "))

bmi = round( weight / height ** 2)

if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinical obese")
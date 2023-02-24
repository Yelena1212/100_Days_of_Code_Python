# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Ticket price is $5")
#     elif age <= 18:
#         print("Ticket price is $7")
#     else:
#         print("Ticket price is $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/ pow(height, 2))

if bmi < 18.8:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")



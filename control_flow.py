# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# #
# bill = 0
# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Children ticket price is $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth ticket price is $7")
#     elif 45 <= age <= 55:
#         print("Have a free ride with us!")
#     else:
#         bill = 12
#         print("Adult ticket price is $12")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#     # Add $3 to the bill
#         bill += 3
#     print(f"You final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")



# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bmi = round(weight/ pow(height, 2))
#
# if bmi < 18.8:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")



# 💪This is a Difficult Challenge 💪
# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
#
# https://www.youtube.com/watch?v=xX96xng7sAE
#
# This is how you work out whether if a particular year is a leap year.
#
# on every year that is evenly divisible by 4
#
# **except** every year that is evenly divisible by 100
#
# **unless** the year is also evenly divisible by 400
#
# e.g. The year 2000:
#
# 2000 ÷ 4 = 500 (Leap)
#
# 2000 ÷ 100 = 20 (Not Leap)
#
# 2000 ÷ 400 = 5 (Leap!)
#
# So the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
#
# 2100 ÷ 4 = 525 (Leap)
#
# 2100 ÷ 100 = 21 (Not Leap)
#
# 2100 ÷ 400 = 5.25 (Not Leap)

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
#     print(f"{year} is Leap year")
# else:
#     print(f"{year} is Not Leap year")

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")


# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."
# e.g.
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total1 = 0
total2 = 0

both_names = (name1 + name2).lower()

total1 += both_names.count("t")
total1 += both_names.count("r")
total1 += both_names.count("u")
total1 += both_names.count("e")

total2 += both_names.count("l")
total2 += both_names.count("o")
total2 += both_names.count("v")
total2 += both_names.count("e")

total = int(str(total1) + str(total2))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

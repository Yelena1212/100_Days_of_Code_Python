# print("123" + "345")
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print(type(new_num_char))
# print("Your name has " + new_num_char + " characters")

# a = float(123)
# print(type(a))
# # print(70 + float("100.5")
# print(str(70) + str(100))

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi = float(weight) / (float(height) ** 2)
# print(int(bmi))

# print(round(8 / 3, 2))
# print(8 // 3)  #make a result int type
#
# print(4 / 2) #return floating type
#
# score = 0
# height = 1.8
# inWinning = True
# #f-String
# print(f"Your score is {score}, your height is {height}, you are winning is {inWinning}")

# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# https://waitbutwhy.com/2014/05/life-weeks.html
#
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y and z are replaced with the actual calculated numbers.
#
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
#
# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# years = 90 - int(age)
# months = years * 12
# weeks = years * 52
# days = years * 365

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What the total bill? "))
tips = int(input("What precentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_presantage = tips / 100
total_tips = total_bill * tip_as_presantage
total_bill_with_presantage = total_bill + total_tips
total_for_each = total_bill_with_presantage / people
final_amount1 = round(total_bill_with_presantage / people, 2)

final_amount = "{:.2f}".format(total_for_each)
print(f"Each person should pay: ${final_amount}")

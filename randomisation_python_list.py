# ___________________________________________________Instructions_______________________________________________
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
#
# e.g. 1 means Heads 0 means Tails

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
# import random
#
# # Write the rest of your code below this line 👇
# random_integer = random.randint(0, 1)
# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")

# ______________________________________________________________________
# states_of_america = ["Delaware", "Washington", "Oregon", "California"]
# print(states_of_america[1])
# states_of_america.append("Arizona")
# states_of_america.extend(["Florida", "Kansas"])
# print(states_of_america)
# ______________________________________________________


# ___________________________Instructions__________________________________________________________________
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!
# Hint
# You might need the help of the len() function.
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
#
# Remember that Lists start at index 0!
# Import the random module here
# import random
#
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# random_integer = random.randint(0, len(names))
#
# if random_integer == 0:
#     print(f"Angela is going to buy the meal today!")
# elif random_integer == 1:
#     print(f"Ben is going to buy the meal today!")
# elif random_integer == 2:
#     print(f"Jenny is going to buy the meal today!")
# elif random_integer == 3:
#     print(f"Michael is going to buy the meal today!")
# else:
#     print(f"Chloe is going to buy the meal today!")
#_____________________________________________________________________________
# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# random_chose = random.randint(0, len(names))
# person_who_will_pay = names[random_chose]
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")

#____________________________________ Instructions_____________________________________
# You are going to write a program that will mark a spot with an X.
#
# In the starting code, you will find a variable called map.
#
# This map contains a nested list. When map is printed this is what the nested list looks like:
#
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
#
# The first digit in the input will specify the column (the position on the horizontal axis).
#
# The second digit in the input will specify the row number (the position on the vertical axis).
# Example Input 1
# column 2, row 3 would be entered as:
#
# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
map[vertical -1][horizontal -1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


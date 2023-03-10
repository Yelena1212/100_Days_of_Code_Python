import os
from subprocess import call
from replit import clear


from art_action import logo
# def clear():
#     # check and make call for specific operating system
#     _ = call('clear' if os.name == 'posix' else 'cls')

# HINT: You can call clear() to clear the output in the console.
print(logo)
bidders_info = {}
flag = False;
while not flag:
    name = input("What is your name? \n")
    bid_price = int(input("What's your bid? \n"))
    bidders_info[name] = bid_price

    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question == "yes" or question == "Yes":
        clear()
    else:
        winner = max(bidders_info, key=bidders_info.get)
        print(f"The winner is {winner} with a bid of ${bidders_info[winner]}")
        flag = True



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

game_list = [rock, paper, scissors]
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_chose > 2 or user_chose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_list[user_chose])

    computer_chose = random.randint(0, 2)
    print("Computer chose:")
    print(game_list[computer_chose])

    if user_chose == computer_chose:
        print("It's a draw")
    elif user_chose == 0 and computer_chose == 2:
        print("You win!")
    elif computer_chose > user_chose:
        print("You lose")
    elif computer_chose == 0 and user_chose == 2:
        print("You lose")
    elif user_chose > computer_chose:
        print("You win!")

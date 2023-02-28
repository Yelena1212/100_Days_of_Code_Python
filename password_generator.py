# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_length = nr_letters + nr_symbols + nr_numbers
print(password_length)

# password = ''

# for n in range(nr_letters):
#   password += random.choice(letters)

# for n in range(nr_symbols):
#   password += random.choice(symbols)

# for n in range(nr_numbers):
#   password += random.choice(numbers)

# print(password)


# ________________________________________________________________


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_total_1 = letters + symbols + numbers
# password_total_2 = list(password_total_1)
# random.shuffle(password_total_2)
# # password_total_3 = ''.join(password_total_2)
# # print(f"Your Password is {password_total_3}")

# for n in range(password_length):
#   password += random.choice(password_total_2)

# print(password)
# ________________________________________________________________


password_list = []
for n in range(nr_letters):
    password_list.append(random.choice(letters))

for n in range(nr_symbols):
    password_list.append(random.choice(symbols))

for n in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
new_password = ''
for char in password_list:
    new_password += char

print(f"Your password is: {new_password}")
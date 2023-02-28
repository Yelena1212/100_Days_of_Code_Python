fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#
# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
#
# Example Output
# 171

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# sum = 0
# count = 0;
# for height in student_heights:
#     sum += height
#     count += 1
# print(sum)
# average = round(sum / count)
# print(average)

# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
#
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#
# The highest score in the class is: x
#
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
#
# Example Output
# The highest score in the class is: 91

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# max = student_scores[0]
# for m in student_scores:
#     if m > max:
#         max = m
#
# print(f"The highest score in the class is: {max}")


total = 0
for number in range(1, 101):
    total += number

# Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#
# Your program should print each number from 1 to 100 in turn.
#
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
#
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# .... etc.
#
# Hint
# Remember your answer should start from 1 and go up to and including 100.
# 2. Each number/text should be printed on a separate line.

#Write your code below this row 👇

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

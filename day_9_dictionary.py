programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

#Adding new item to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
# Create an empty dictionary
empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth of your computer"


#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    # print(programming_dictionary[key])


#_______________________________________________________
#Instructions
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the
# values are their exam scores.
#
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
#
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
#
# DO NOT write any print statements.
#
# This is the scoring criteria:
#
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"
#
# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.
#
# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.
#
# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.
#__________________________________________________________________________________________________________________
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if 91 < student_scores[key] < 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
# print(student_grades)
#_______________________________________________________________\

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Russia": {"cities_visited": ["Tomsk", "Moscow", "Omsk"], "total_visits": 3},
}

# Nesting Dictionary in a List
#
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12
#     },
#     {
#         "country": "Russia",
#         "cities_visited": ["Tomsk", "Moscow", "Omsk"],
#         "total_visits": 3
#     },
# ]

#_________________________________________________________________
# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
#
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
#
# You've been to Moscow and Saint Petersburg.
#
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
#
# Hint
# Look at the function call above to see what the name of the function should be.
#
# The inputs for the function are positional arguments. The order is very important.
#
# Feel free to choose your own parameter names.
#____________________________________________________________________________________________

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

"""Exercises - Day 2
Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords"""

# Exercises: Level 1
# Write a python comment saying 'Day 2: 30 Days of python programming'
print("Day 2: 30 Days of python programming")
# Declare a first name variable and assign a value to it
first_name = 'Matt'
# Declare a last name variable and assign a value to it
last_name = 'Hurrell'
# Declare a full name variable and assign a value to it
full_name = first_name + last_name
# Declare a country variable and assign a value to it
country = 'Australia'
# Declare a city variable and assign a value to it
city = 'Canberra'
# Declare an age variable and assign a value to it
age = 25
# Declare a year variable and assign a value to it
year = 1999
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line
first_name, last_name = 'Matt', 'Hurrell'

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
all_variables = [first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on]
for x in all_variables:
    print(type(x))
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("First name is bigger by: ", len(first_name) - len(last_name))
elif len(first_name) < len(last_name):
    print("Last name is bigger by: ", len(last_name) - len(first_name))
else:
    print("Names are same size")
    
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("Total is: ", total)
# Subtract num_two from num_one and assign the value to a variable diff
variable_diff = num_two - num_one
print("Variable diff is: ", variable_diff)
#Multiply num_two and num_one and assign the value to a variable product
variable_product = num_two * num_one
print("Variable product is: ", variable_product)
# Divide num_one by num_two and assign the value to a variable division
variable_division = num_one/num_two
print("Variable division is: ", variable_division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
variable_remainder = num_two % num_one
print("Variable remainder is: ", variable_remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
variable_exp = num_one** num_two
print("Variable exp is: ", variable_exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_divison = num_one//num_two
print("Variable floor division is: ", floor_divison)

# The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
import math
area_of_circle = math.pi*(radius**2)
print("Area of a circle with radius of 30 is: ", radius)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi*radius
print("Cicuumference of a circle with radius of 30 is: ", circum_of_circle)

# Take radius as user input and calculate the area.
radius = int(input("What is the radius of the cirlce? Please enter a integer: " ))
area_of_circle = math.pi * (radius**2)
print("Area of a circle with radius of ",radius, " is:  ", area_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What is your country name? ")
age = int(input("What is your age? "))

all_variables = [first_name, last_name, country, age]

for x in all_variables:
    print(x)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords"""
help('keywords')
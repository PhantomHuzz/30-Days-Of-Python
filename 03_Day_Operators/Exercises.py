"""Exercises - Day 3
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""

# Declare your age as integer variable
age = 25

# Declare your height as a float variable
height = 5.11
#Declare a variable that store a complex number
complex_num = 1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
## The area of the triangle should be  100

base = None
height = None
base = int(input("Please Enter base (20): "))
height = int(input("Please Enter height (10): "))
area = (0.5 * base * height)
print("The area of the triangle is: ", int(area))
    
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
sidea = int(input("Please Enter side a (5): "))
sideb = int(input("Please Enter side a (4): "))
sidec = int(input("Please Enter side a (3): "))
perimeter = (sidea + sideb + sidec)
print("The perimeter of the triangle is: ", int(perimeter))

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
width = int(input("Please Enter width a (5): "))
length = int(input("Please Enter length a (4): "))
perimeter = (2 * (length + width))
area = (length * width)
print("The perimeter of the rectangle is: ", int(perimeter))
print("The area of the rectangle is: ", int(area))


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius = int(input("Please Enter radius of the circle: "))
area = (math.pi * radius * radius)
circumference = (2 * math.pi * radius)
print("The area of the circle is: ", area, " and the circumference is: ", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

# Points for slope and distance calculation
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope (m) between the points
slope_points = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance between the points
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Given equation y = 2x - 2
m_equation = 2  # The slope of the equation
y_intercept = -2  # The y-intercept of the equation
x_intercept = -y_intercept / m_equation  # Solving for x-intercept when y = 0

print(slope_points, distance, m_equation, y_intercept, x_intercept)


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Loop to print y for multiple x values and check when y is 0
for x in range(-10, 11):  # Test x from -10 to 10
    y = (x**2 + 6*x + 9)
    print(f"For x = {x}, y = {y}")
    
    # Check if y is 0
    if y == 0:
        print(f"y is 0 when x = {x}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = 'Python'
dragon = 'Dragon'
print("The length of Python is: ", len(python), " and the length of Dragon is: ", len(dragon))
if len(python) == len(dragon):
    print ("not the same length hehe")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in python and dragon:
    print("In both")
else:
    print("no luck")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
# Use in operator to check if jargon is in the sentence.
if "jargon" in sentence:
    print("jargon is in the sentence")
else:
    print("No luck kiddo")

# Find the length of the text python and convert the value to float and convert it to string
length_of_python = len(python)
print(length_of_python)
float_python = float(length_of_python)
print(float_python)
string_python = str(float_python)
print(string_python)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numbers = 10,3,4,5,1,2

for x in numbers: 
    if x % 2 == 0:
        print(x, " is an even number")
    else:
        print(x, " is not an even number")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = (7/3)
value = 2.7

if floor_div == int(value):
    print("floor division of 7 by 3 is equal to the int converted value of 2.7 ")
else: 
    print("Unlucky bud")

#Check if type of '10' is equal to type of 10

if type('10') == type(10):
    print("type of '10' is equal to type of 10")
else: 
    print("type of '10' is not equal to type of 10")

# Check if int('9.8') is equal to 10
if int(9.8) == 10:
    print("int('9.8') is equal to 10")
else: 
    print("int('9.8') is not equal to 10")

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
rate = int(input("Please enter rate per hours in int (28): "))
hours = int(input("Please enter hours in int (40): "))
weekly_earning = rate * hours
print("Your weekly earning is $", weekly_earning)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Please enter number of years you will live: "))
seconds = years * 365 * 24 * 60 * 60
print("Number of seconds you will live: ", seconds)

# Write a Python script that displays the following table
print("""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")
"""💻 Exercises - Day 1
Exercise: Level 1
1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
3. Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
4. Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
Exercise: Level 2
5. . Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
6. . Find an Euclidian distance between (2, 3) and (10, 8)
🎉 CONGRATULATIONS ! 🎉"""

#1 Check the python version you are using
# python3 --version

#2 Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
print(3+4)
# subtraction(-)
print(3-4)
# multiplication(*)
print(3*4)
# modulus(%)
print(3%4)
# division(/)
print(3/4)
# exponential(**)
print(3**4)
# floor division operator(//)
print(3//4)

# 3. Write strings on the python interactive shell. The strings are the following:
# Your name
print("Matt")
# Your family name
print("Hurrell")
# Your country
print("Australia")
# I am enjoying 30 days of python
print("I am enjoying 30 days of python")

# 4. Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type (4-4j))
#['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type("Matthew"))
#Your family name
print(type("Hurrell"))
# Your country
print(type("Australia"))

# 5. . Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Number(Integer, Float, Complex),
print(type(5))
print(type(0.5))
print(type(1j))
# String
print(type("example"))
# Boolean
print(type(True))
# List
print(type([1,2,3,4]))
# Set
print(type({1,3,4,2}))
# Dictionary
print(type({1: "Hello",3: "hi", 4:"Boo"}))

# 6. . Find an Euclidian distance between (2, 3) and (10, 8)
import math
#Formula
print("d(p, q) = √((p₂ - p₁)² + (q₂ - q₁)²)")
# Coordinates of the points 
p1, q1 = 2, 3  # Point 1 (2, 3)
p2, q2 = 10, 8  # Point 2 (10, 8)
# Calculate
euclidean_distance = math.sqrt(((p2 - p1)**2) + ((q2 - q1)**2))
# Print
print("Euclidean distance:", euclidean_distance)

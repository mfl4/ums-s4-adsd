# Comments
# print something
print("Hello, World!")

# Variables
name = "MFL4"

# Input
fav = input("Enter your favorite food: ")
print("Thank you. Data saved.")
print("Your favorite food is " + fav)

# Data types
## Numerical data types: integer, float and boolean
a = 33
b = 33.33
c = True
## Character and string data types
characters = 'c'
strings = "my name is MFL4"
alphabet = strings[0]
## casting
num = 32
num_str = str(num)
sum = num_str + num_str

# Operations
## Math operations: addition, subtraction, multiplication, division(types matters), division(quotient), exponentiation
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
c = a % b
c = a ** b
## Comparison operations: boolean
a = 10
b = 3
c = a > b
d = a < b
e = a == b
f = a != b
g = a >= b
h = a <= b
## Logical operations
a = 10
b = 3
c = a > b and a < b
d = a > b or a < b
e = not a > b
## Bitwise operations
a = 10
b = 3
c = a & b
d = a | b
e = a ^ b
f = ~a
g = a << 2
h = a >> 2

# Complex data types
## list (mutable, iteration time)
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, "MFL4"]
## tuple (immutable)
a = (1, 2, 3, 4, 5)
b = (1, 2, 3, 4, 5, "MFL4")
## dictionary
a = {"name": "MFL4", "age": 33, "address": "Jakarta"}
b = {"name": "MFL4", "age": 33, "address": "Jakarta", "hobbies": ["music", "reading"]}

# conditional statements (elif optional)
a = 10
b = 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# looping
# collections loop
## collection loop: for
a = [1, 2, 3, 4, 5]
for x in a:
    print(x)
b = {"name": "MFL4", "age": 33, "address": "Jakarta"}
for x in b:
    print(x)
for x in b.values():
    print(x)
for x in b.items():
    print(x)
## conditional loop: while
a = 0
while a < 5:
    print(a)
    a += 1

# Functions
# Without return
def greet_bryan():
    print("Hello, Bryan!")
# With return
def first():
    """return the first item"""
    product = ["shirt", "shoes", "pants", "hats", "shoes"]
    return product[0]
result = first()
print(result)
print(first())
# With return & params
def area_triangle(base, height):
    """return the area of a triangle with input base and height"""
    area = 0.5 * base * height
    return area
print(area_triangle(2,4))

# Recursion: call it self
def factorial(number):
    """  """
    if number == 1  or number == 0:
        return 1
    else:
        return number * factorial(number-1)

num = int(input("Enter a number : "))
print("The factorial of " + str(num) + " is " + str(factorial(num)))
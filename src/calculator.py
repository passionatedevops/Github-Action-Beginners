# python code for a simple calculator

# Function to add two numbers
import math


def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to calculate the power of a number
def power(x, y):
    return x ** y

# Function to calculate the square root of a number
def square_root(x):
    return x ** 0.5

# Function to calculate the factorial of a number
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
# Function to calculate the absolute value of a number
def absolute_value(x):
    return abs(x)

# Function to calculate the remainder of a number
def remainder(x, y):
    return x % y

# Function to calculate the average of two numbers
def average(x, y):
    return (x + y) / 2

# Function to calculate the maximum of two numbers
def maximum(x, y):
    return max(x, y)

# Function to calculate the minimum of two numbers
def minimum(x, y):
    return min(x, y)

# Function to calculate the square of a number
def square(x):
    return x ** 2

# Function to calculate the cube of a number
def cube(x):
    return x ** 3

# Function to calculate the inverse of a number
def inverse(x):
    return 1 / x   

# Function to calculate the sine of a number
def sine(x):
    return math.sin(x)

# Function to calculate the cosine of a number
def cosine(x):
    return math.cos(x)

# Function to calculate the tangent of a number
def tangent(x):
    return math.tan(x)

#test min with two positive numbers

def test_min():
    assert minimum(2, 3) == 2
    print("Test passed")


#call  test_min function

test_min()



    
    


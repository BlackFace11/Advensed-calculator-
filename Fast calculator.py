#python 3.7.1
#copyright 2023 2024 by glox studio 
print ("Welcome to Fast Calc BETA")

# Define constants 
PI = 3.14159

# Define functions
def addition(num1, num2): 
    return num1 + num2

def subtraction(num1, num2): 
    return num1 - num2

def multiplication(num1, num2): 
    return num1 * num2

def division(num1, num2): 
    return num1 / num2

def modulus(num1, num2): 
    return num1 % num2

def exponent(num1, num2): 
    return num1 ** num2

# Get user input
print("This program implements an advanced calculator capable of performing basic arithmetic operations, exponentials, scientific notation,By glox studio ")
print ("_____________________________________________________________________________________________________________________________________________ ")
num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
operation = input("(+, -, *, /, %, **): ")

# Convert user input to integers
num1 = int(num1)
num2 = int(num2)

# Perform operation
if operation == "+": 
  result = addition(num1, num2)
elif operation == "-": 
  result = subtraction(num1, num2)
elif operation == "*": 
  result = multiplication(num1, num2)
elif operation == "/": 
  result = division(num1, num2)
elif operation == "%": 
  result = modulus(num1, num2)
elif operation == "**": 
  result = exponent(num1, num2)
else: 
  print("Error: Unknown operator")

# Print result 
print("Result is " + str(result))
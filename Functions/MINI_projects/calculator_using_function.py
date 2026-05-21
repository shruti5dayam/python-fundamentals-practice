# =====================================
# Calculator Using Functions
# =====================================

# Addition Function

def add(a,b):
    return a+b

# Subtraction Function

def subtract(a,b):
    return a-b

# Multiplications Function

def multiply(a,b):
    return a*b

# Division Function

def division(a,b):
    if b == 0 :
        return "Cannot divide by zero"
    return a/b

# User Input
num_1 = float(input("Enter frist number: "))
num_2 = float(input("Enter second number: "))

# Function Calls
print("Addition: ",add(num_1,num_2))
print("Subtraction: ",subtract(num_1,num_2))
print("Multiplication: ",multiply(num_1,num_2))
print("Division: ",division(num_1,num_2))

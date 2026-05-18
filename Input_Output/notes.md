# Input / Output
## Definition 
Input means taking data from the user.

Output means displaying data to the user.

Python mainly users:
- input()
- print()

--------------

# Input 
Used to take user data.

Examples:
name = input("Enter your name:")

----------------

# Output 
Used to display information.

Example:
print("Hello")

-----------------

# IMPORTANT RULE 
input() ALWAYS store data as string.

Example:

age = input("Enter age:")

Even if user types:

24 

Python stores it as :

"24"

-----------------------

# Type Conversion 
Convert input into correct type.

Example:

age = int(input("Enter age: "))

--------------- 

# Formatted Output 
Used to print variables nicely.

Example:

name = "Shruti"

print(f"Welcome {name})

----------------
# Common Mistakes 
## 1. Forgetting type conversion 
BAD: 

age = input("Enter age:")

print(age+ 5)

GOOD: 

age = int(input("Enter age:"))

print(age + 5)

-------------------

## 2. Missing quotes in print 

BAD:

print(Hello)

GOOD: 

prin("Hello")

-----------------

# Backend Connection 

Backend applications constantly take input.

Backend applications constantly take input:
- login forms
- passwords
- API requests 
- search fields
- chatbot messages 

And return output:

- responses
- JSON data 
- success messages 
- errors

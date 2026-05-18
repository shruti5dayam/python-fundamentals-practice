## Definition 
Data types define the kind of value stored inside a variable.

Python uses different data types for :
- text
- numbers
- ture/false values
- collection of data

-----------

## Main Data Types

### 1. String (str)
Used for text. 

Example:
name = "Shruti"
--------------
### 2. Integer (int)
used for whole numbers.

Example: 
age = 24
------
### 3. Float (float)
Used for decimal numbers.

Example: 
height = 5.4
--------
### 4. Boolean(bool)
Used for Ture/False values.

Example: 
is_logged_in = True
------------
### 5. List (list)
Stores multiple values.

Example:
numbers = [1,,2,3]
---------
### 6. Dictionary (dict)
Stores data in key-value format.

Example: 
user = { 
"name": "Shruti"
}
---------
## type() function
used to check data type

Example:
print(type(age))
-----------
## Type Conversion 
Convert one type into another 
### String into Integer  
age = int("24")
### Integer to Float 
price = float(50)
### Float to Integer
number = int(5.9)

--------
## NOTE:
### Python automatically understands the type 
### input() - Python always takes string by default

--------------

## Common Mistakes 

### 1. Adding string and integer 
BAD: 
age = int("24") + 5 
GOOD:
age = int("24") + 5

--------------
### 2. Forgetting quotes 
BAD: 
name = shruti 
GOOD: 
name = "Shruti"
--------------

## Backend Connection
Backend systems use data types constantly:
- usernames -> string
- age -> integer
- salary -> float
- login status -> boolean
- API responses -> dictionary 


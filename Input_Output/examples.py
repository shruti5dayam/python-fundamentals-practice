# =======================================
# INPUT / OUTPUT Examples
# =======================================

# ---------------------------------------
# Example 1 - Simple Output
# ---------------------------------------

print("Welcome to Python")

# --------------------------------------
# Example 2- User Input
# --------------------------------------

name = input("Enter your name: ")
print(name)

# --------------------------------------
# Example 3 - Formatted Output
# ---------------------------------------

city = "New Jersey"

print(f"I live in {city}")

# --------------------------------------
# Example 4 - Internet Input
# --------------------------------------


age = int(input("Enter your age: "))

print(age)

# --------------------------------------
# Example 5 - Float Input
# --------------------------------------

height = float(input("Enter your height: "))

print(height)

print(type(height))

# --------------------------------------
# Example 6 - Addition Using Input
# --------------------------------------

num_1 = int(input("Enter first numer: "))
num_2 = int(input("Enter second number: "))
sum = num_1 + num_2
print(sum)

# --------------------------------------
# Example 7 - Multiple Outputs
# --------------------------------------

username = "shruti5dayam"
followers = 500
print("username:",username) # the space already comes os just one space after :
print("followers: ",followers) # it wil result in double space after :

# ---------------------------------------
# Example 8 - Backend Style Example
# ---------------------------------------

email = input("Enter email:")
password = input("Enter password:")

print(f"Login attempted for {email}")

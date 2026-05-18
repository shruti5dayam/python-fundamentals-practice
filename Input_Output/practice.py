# =======================================
# Input / Output Practice
# =======================================

# --------------------------------------
# Practice 1
# Ask username and print welcome message
# --------------------------------------

username = input("enter username: ")
print(f"Welcome {username}")

# -------------------------------------
# Practice 2
# Ask age and print it
# -------------------------------------

age = int(input("Enter your age: "))

print(age)

# -------------------------------------
# Practice 3
# Ask 2 numbers and print total
# -------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print(total)

# --------------------------------------
# practice 4
# Ask marks and Calculate average
# ---------------------------------------

marks_maths = float(input("Enter you Maths marks: "))
marks_chemistry = float(input("Enter you Chemistry marks: "))
marks_physics = float(input("Enter you Physics marks: "))
total_marks = marks_chemistry + marks_physics + marks_maths
average = total_marks/3
print(total_marks)
print(average)

# -------------------------------------------
# Practice 5
# Ask city and country
# ---------------------------------------------

city = input("Enter your City: ")
country = input("Enter your Country: ")

print(f"You live in {city}, {country}")

# -----------------------------------------------
# practice 6
# Backend style practice
# -----------------------------------------------

email = input("Enter your email: ")
password = input("Enter your password: ")

print(f"Login request received")
print(f"User email: {email}")




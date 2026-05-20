# ======================================
# Age credentials checker
# ======================================

age = int(input("Enter your age: "))

# Voting eligibility
if age >=18:
    print("You are eligible for voting")
else:
    print("You are not eligible")

# Driving eligibility
if age >=16:
    print("You are eligible fro driving")
else:
    print("You are not eligible for driving")

# Login Credentials
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")





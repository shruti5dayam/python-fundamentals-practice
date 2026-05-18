# ================================
# Data Types Practice
# ===============================
from Variables.practice import followers

# -------------------------------
# Practice 1
# Create variables of different types and print
# ----------------------------------

given_name = "Shruti"
surname = "Dayam" # string
age = 24 #int
height = 5.2 #float
lives_in_USA = True #boolean
flowers = ["rose", "lily", "sunflower"] #lists
address = {
    "City": "Jersey City",
    "State": "NJ"
}
print(surname)
print(age)
print(height)
print(lives_in_USA)
for flower in flowers:
    print(flower)

print(address)

# ---------------------------------------
# Practice 2
# Convert string to integer
# --------------------------------------

score_text = "80"
score_number = int(score_text)
print(type(score_number))
print(score_number)

# --------------------------------------
# Practice 3
# Convert integer to float
# ------------------------------------------

salary = 500
salary_float = float(salary)

print(salary_float)
print(type(salary_float))

# ----------------------------------------------
# Practice 4
# Convert float to integer
# -----------------------------------------------

rating = 4.9
final_rating = int(rating)

print(final_rating)
print(type(final_rating))

# -----------------------------------------------
# Practice 5
# Indentify data types
# ------------------------------------------------

username = "backend_dev"
follower = 500
rating = 4.8
is_verified = False

print(type(username))
print(type(follower))
print(type(rating))
print(type(is_verified))

# --------------------------------------------------
# Practice 6
# Backend style practice
# ---------------------------------------------------

response = {
    "status_code":200,
    "is_success": True,
    "data": ["user1","user2"] # lists in dictionaries
}

print(type(response))


# =========================
# Data Types Examples
# ========================

# -----------------------
# Example 1 - String
# ----------------------

name = "Shruti"
print(name)
print(type(name))

# ------------------------
# Example 2 - Integer
# -----------------------

age = 24
print(age)
print(type(age))

# --------------------------
# Example 3 - Float
# -------------------------
PI = 3.14
print(PI)
print(type(PI))

height = 5.2
print(height)
print(type(height))

# ---------------------------
# Example 4 - Boolean
# ---------------------------

is_student = True
print(is_student)
print(type(is_student))

# -------------------------
# Example 5 - List
# -------------------------

numbers = [1,2,3]
print(numbers)
print(type(numbers))

# -----------------------
# Example 6 - Dictionary
# -----------------------
user = {
    "name": "Shruti",
    "country": "USA"
}
print(user)
print(type(user))

# ------------------------
# Example 7 - String to Integer
# -------------------------

age_text = "25"
print(type(age_text))
age_number = int(age_text)
print(age_number)
print(type(age_number))

# -------------------------
# Example 8 - Integer to Float
# --------------------------

price = 100
new_price = float(price)

print(new_price)
print(type(new_price))

# -----------------------
# Example 9 - Float to Integer
# ----------------------

score = 99.9
new_score = int(score)
print(new_score)
print(type(new_score))

# --------------------------
# Example 10 - Backend style example
# ---------------------------
api_response = {
    "status": 200,
    "success": True,
    "message": "Login successful"
}

print(api_response)

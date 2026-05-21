# =========================================
# Function - Practice Problems
# =========================================

# -----------------------------------------
# Practice Problem 1
# Square Function
# ----------------------------------------

def square(number):
    return number*number

print(square(5))

# ------------------------------------------
# Practice Problem 2
# Even and Odd Function
# ------------------------------------------

def check_even(number):
    if number %2 == 0:
        print("even")
    else:
        print("Odd")

check_even(8)

# --------------------------------
# Practice Problem 3
# Maximum number
# ---------------------------------

def find_max(a,b):
     if a>b:
        return a
     else:
        return b

print(find_max(5,3))


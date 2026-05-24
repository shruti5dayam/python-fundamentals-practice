# ==========================================
# Practice Problems
# ===========================================

# -------------------------------------------
# Practice 1
# Global Variable
# -------------------------------------------

company = "OpenAI"

def show_company():
    print(company)

show_company()

# --------------------------------------------
# Practice 2
# Local Variable
# --------------------------------------------

def student():
    student_name = "Shruti"
    print(student_name)

student()

# ----------------------------------------------
# Practice 3
# Scope Difference
# ----------------------------------------------

number = 10

def change_number():
    number = 5
    print("Inside Function: ",number)

change_number()
print("Outside function: ", number)
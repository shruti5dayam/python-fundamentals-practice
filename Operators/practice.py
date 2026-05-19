# ===========================================
#  Operators Practice Problems
# ==========================================

# ------------------------------------------
# Practice 1
# Calculator
# ------------------------------------------

num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter you second number: "))

print("Addition:", num_1+num_2)  # it doesnt matter if there is
print("Subtraction:", num_1-num_2) # space or not after,(comma)
print("Multiplication:",num_1*num_2) # in the print function the space
print("Division:",num_1/num_2) #only after : colon add it not after ,
print("Power:", num_1**num_2)

# ---------------------------------------------
# Practice 2
# Percentage Calculator
# ---------------------------------------------

marks = float(input("Enter your marks:"))
total = float(input("Enter your total marks:"))

percentage = (marks/total)*100
print(f"Your percentage is {percentage}")
print("Percentage:",percentage)

# ------------------------------------------------
# Practice 3
# Comparison Checker
# -------------------------------------------------

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

print("Equal:", num1==num2)
print("Greater:", num1>num2)
print("Lesser:", num1<num2)


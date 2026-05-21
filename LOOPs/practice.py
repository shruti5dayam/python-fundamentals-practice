# ============================================
# LOOPs Practice Problems
# ============================================

# --------------------------------------------
# Practice 1
# Print Numbers
# --------------------------------------------

for i in range(1,11):
    print(i)

# --------------------------------------------
# Practice 2
# Even Numbers
# --------------------------------------------

for i in range(1,21):

    if i % 2 == 0: # only whe remainder is 0 it will print that number
        print(i)


# ---------------------------------------------
# Practice 3
# Sum of Numbers
# ----------------------------------------------


total = 0

for i in  range(1,10):
    total += i

print("Total: ", total)


# ---------------------------------------------------
# Practice 4
# Multiplication Table
# ---------------------------------------------------

number = int(input("Enter a number:  "))

for i in range(1,11):
    print(number, "x", i, "=", number*i)

# ---------------------------------------------------
# My trial Practice
# squaring the numbers
# -----------------------------------------------------

num = int(input("Enter a number: "))

count = 1

while count <= 3:
    print("Current number: ", num)
    num = num*num
    count += 1




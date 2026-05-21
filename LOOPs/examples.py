# =============================================
# LOOPs Examples
# ===============================================


# ------------------------------------
# FOR Loop example
# ------------------------------------

for i in range(1,6): # will print till 5 so from a to b-1 in range(a,b)
    print(i)

# -----------------------------------
# WHILE Loop example
# -----------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1

# --------------------------------------
# Break example
# --------------------------------------

for number in range(1,10):
    if number ==5:  # it will break 5 and will only print till 4
        break

    print(number)

# ---------------------------------------
# CONTINUE example
# ---------------------------------------

for number in range(1,6):
    if number ==3:  # it will skip 3 and will print rest 1 2 4 5
        continue

    print(number)


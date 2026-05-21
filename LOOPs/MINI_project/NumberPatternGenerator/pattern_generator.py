# ================================
# Triangle Pattern
# ================================

rows = 5

for i in range(1, rows+1):
    print("*" * i)

# "*" is a string
# Multiplying string × number repeats the string
# "*" * 3 → "***"
# STRING REPETITION


# print("*", *i)
# The comma changes the meaning completely.
# *i tries to unpack i as an iterable.
# But i is an integer, and integers are NOT iterable.
# This causes:
# TypeError: Value after * must be an iterable
# NUMBER MULTIPLICATION


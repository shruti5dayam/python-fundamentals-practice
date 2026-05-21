total = 0
subjects = 5

for i in range(subjects): # here "i" is loop counter/index to repeat the loop 5 times
    marks = float(input("Enter your marks: "))
    total += marks
# i=0 to i = 4 so 5 times - Python automatically changes it to this
average = total / subjects

print("Average: ",average)

if average > 90:
   print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 50:
    print("Grade C")
else:
    print("Fail")

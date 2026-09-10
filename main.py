import sys

mark1 = float(sys.argv[1])
mark2 = float(sys.argv[2])
mark3 = float(sys.argv[3])

total = mark1 + mark2 + mark3
average = total / 3

print("Subject 1:", mark1)
print("Subject 2:", mark2)
print("Subject 3:", mark3)
print("Total:", total)
print("Average:", average)

if average >= 40:
    print("PASS")
else:
    print("FAIL")
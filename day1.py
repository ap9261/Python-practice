# Basics
# Print your name, college, and branch.
# Take two numbers and print their sum.
# Take a number and print its square.
# Check if a number is even or odd.
# Check voting eligibility.
# Loops
# Print 1 to 10.
# Print 10 to 1.
# Multiplication table.
# Sum from 1 to n.
# Count digits in a number.

print("Atharv ,AISSMS IOIT, AI&DS")

a = 4
b = 5

sum = a+b
print(sum)

num = int(input("Enter a number"))
square = num**2
print(square)

n = int(input("Enter a num to check even or odd"))
if n%2 == 0:
    print("Even")
else:
    print("Odd")

vote = int(input("enter u r age"))
if vote>=18:
    print("You can vote ")
else:
    print("Cant")

print("Printing 1 to 10")

nom = 10
for i in range (nom):
    print(i)


for i in range (10 -1 -1):
    print(i)
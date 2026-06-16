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

print("Printing 1 to 10 ")

for i in range (1,11):
    print(i)
print("Printing 10 to 1")

for i in range (10,-1,-1):
    print(i)

num1 = int(input("enter num u want table"))

for i in range(1,11):
    table = print(f"{num1}X{i}={num1*i}")

nom = int(input("Enter num of n to sum"))

sum = 0

for i in range(1,nom+1):
    sum+=i

print(sum)


c = int(input("Enter a number to count digits: "))

count = 0

# If the user enters 0, it still has 1 digit
if c == 0:
    count = 1
else:
    while c > 0:
        c = c // 10  # This removes the last digit (e.g., 523 becomes 52)
        count += 1   # Add 1 to the digit count

print(f"The number of digits are {count}")

name = "Atharv"

reversed_name = name[::-1]

print(reversed_name)

vowels = ['a','e','i','o','u']

count = 0

n = str(input("Enter a name to count vowels"))

for i in n:
    if i.lower() in vowels:
        count = count + 1

print("Total numbers of vowels in name are",count)

nam = "ata"

pal = nam[::-1]

if pal == nam:
    print("Palindrome")
else:
    print("Not Palindrome")

maxi = [10,20,55,40,23]

highest = maxi[0]
for i in maxi:
    if i > highest:
        
        highest = i
    
print("Max",highest)

mini = [10,20,55,40,23]

minimum = mini[0]
for i in mini:
    if i < minimum:
        
        minimum = i
    
print("Min",minimum)

list = [1,2,3,4,5,6,7,8]

rev_list = list[::-1]

sum = 0 

for i in list:
    sum+=i


print("Reverse list",rev_list)
print("Sum of list",sum)

def cal():

    print("!!!Calculator!!!")

    a = float(input("Enter a number"))
    b = float(input("Enter a second number"))

    add = a+b
    sub = a-b
    div = a/b
    mul = a*b

    print("Operations Answer of add,sub,div,mul respectively are",add,sub,div,mul)

cal()

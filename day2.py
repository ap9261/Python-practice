def greet():
    print("Hello Atharv!")
    print("Welcome to Python.")

def sum(a,b):
   
    return a + b
def squ(s):
    return s ** 2

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def largest(x,y,z):
    return max(x,y,z)

def fact(num):
    result = 1
    while num > 1:
        result = result * num
        num = num - 1          # Counts down (e.g., 5, then 4, then 3...)
    return result

def is_prime(num):
    if num <= 1:
        return False  # Numbers 1 or less are not prime
        
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a number that divides it perfectly!
            
    return True  # If no numbers divided it, it is prime

# Check the answers:
print(is_prime(7))   # Outputs: True
print(is_prime(10))  # Outputs: False

greet()
print(sum(5,2))
print(squ(5))
even_odd(7)
print(largest(10,55,90))
print(fact(5))

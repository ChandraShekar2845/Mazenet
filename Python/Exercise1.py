# Write a Python program to check if a given number is prime.

n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

print(prime)

# Output:
# C:\Users\chand\Mazenet\Python>python Exercise1.py             
# Enter a number: 29
# True
# C:\Users\chand\Mazenet\Python>python Exercise1.py
# Enter a number: 15
# False'''
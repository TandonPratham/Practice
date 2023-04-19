# Fibonacci series using iterative method
number = int(input("Enter the number : "))
a = 0
b = 1
c = 0
while (c <= number):
    print(c)
    a = b
    b = c
    c = a+b

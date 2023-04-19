# Fibonacci series using recursive method

def fib (number):
    a = 0
    b = 1
    c = 0
    while c <= number:
        print(c)
        a = b
        b = c
        c = a + b

number = int(input("Enter the number : "))
fib(number)

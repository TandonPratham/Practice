# Number is prime number or not

number = int(input("Enter the number : "))
count = 0
i =1
while (i <=number):
    if number % i == 0:
        count = count + 1
    i = i+1

if(count == 2):
    print("It is a prime number")
else:
    print("It is not a prime number")
#pallindrome 

no = int(input("Enter the number = "))
og = no
rev = 0 
while no !=0 :
    rem = no % 10
    rev = rev * 10 + rem
    no //= 10

if rev == og:
    print("Pallindrom")
else:
    print("Not Pallindrome")

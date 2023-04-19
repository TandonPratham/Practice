# Reverse the Number

Number = int(input("Enter the number : "))
Reverse = 0
while (Number > 0):
    Reverse = (Reverse * 10) + Number % 10
    Number = Number // 10
print("Reversed Number is ",Reverse)
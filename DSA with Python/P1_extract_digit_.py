# P1. Extract digits of a given number

x=int(input("Enter a number: "))
digit=x
while digit>0:
    print(digit%10)
    digit=digit//10
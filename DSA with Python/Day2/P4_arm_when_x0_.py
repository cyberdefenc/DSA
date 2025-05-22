import math

x = int(input("Enter a number: "))
arm = 0
digit = x


if x == 0:
    count = 1
else:
    count = int(math.log10(x)) + 1

while digit > 0:
    rev = digit % 10
    pw = rev ** count
    arm += pw
    digit //= 10

if arm == x:
    print("The number", x, "is an Armstrong number")
else:
    print("The number", x, "is not an Armstrong number")

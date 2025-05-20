# P4. Count digits in a given number using log

import math

x=int(input("Enter a number: "))
count=math.log10(x)+1               # log function returns a decimal value (float).
print("Number of digits in",x,"is",int(count))  


# print(count)         # Output: 4.0
# print(int(count))    # Output: 4  #it removes .0

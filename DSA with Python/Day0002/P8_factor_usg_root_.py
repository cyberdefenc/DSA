from math import sqrt

x = int(input("Enter a number: "))
divisors = []

root = int(sqrt(x))

i = 1
while i <= root:
    if x % i == 0:
        divisors.append(i)
        if x // i != i: 
            divisors.append(x // i)
    i += 1

divisors.sort() #sorting time complexity is O(nlogn)
print(divisors)

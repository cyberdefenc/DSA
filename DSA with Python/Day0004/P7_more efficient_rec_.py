def sumton(n):
    if n==1:
        return 1
    return n + sumton(n-1)
x = int(input("Enter a number: "))
result = sumton(x)
print("Sum is:", result)
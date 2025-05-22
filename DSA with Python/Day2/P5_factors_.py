
x=int(input("Enter a number: "))
print("Factors of", x, "are: 1,")
i=2
while i<x:
    if x%i==0:
        print(i,)
    i+=1
print(x)

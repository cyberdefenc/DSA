x=int(input("Enter a number: "))
list=[1]
i=2
while i<=x:
    if x%i==0:
        list.append(i)
    i+=1
print(list)
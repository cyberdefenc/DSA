x=int(input("Enter a number: "))
list=[1,x]
i=2
half=x//2
while i<=half:
    if x%i==0:
        list.append(i)
    i+=1
print(list)
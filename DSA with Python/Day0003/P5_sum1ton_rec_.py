def sumto(sum,i,n):
    if i>n:
        return sum
    sum+=i
    return sumto(sum,i+1,n)

x=int(input("Enter a number: "))
result=sumto(0,1,x)
print(result)
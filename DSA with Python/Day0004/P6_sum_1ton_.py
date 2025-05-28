def sumto(sum,i,n):
    if i>n:
        print("Sum is:", sum)
        return 
    sumto(sum+i,i+1,n)

x=int(input("Enter a number: "))
sumto(0,1,x)

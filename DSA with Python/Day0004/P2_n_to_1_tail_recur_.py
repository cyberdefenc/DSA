
def oneton(i,n):
    if i>n:
        return
    oneton(i+1,n)  # This is Tail Recursion  calling function first then doing job
    print(i)
    


x=int(input("Enter the value of n: "))
oneton(1,x)
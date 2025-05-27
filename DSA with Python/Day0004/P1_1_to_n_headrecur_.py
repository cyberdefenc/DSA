
def oneton(i,n):
    if i>n:
        return
    print(i)
    i+=1
    oneton(i,n)  # This is Head Recursion doing job first then calling function


x=int(input("Enter the value of n: "))
oneton(1,x)
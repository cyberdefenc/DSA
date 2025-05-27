
def oneton(n):
    if n==0:
        return
    oneton(n-1) 
    print(n)
    


x=int(input("Enter the value of n: "))
oneton(x)
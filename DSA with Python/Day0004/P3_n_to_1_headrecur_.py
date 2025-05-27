
def oneton(n):
    if n==0:
        return
    print(n)
    oneton(n-1)  
    


x=int(input("Enter the value of n: "))
oneton(x)
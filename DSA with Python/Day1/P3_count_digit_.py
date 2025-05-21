# P3 Count digits in a given number

x=int(input("Enter a number: "))
count=0
digit=x

while digit>0:
    count+=1
    digit=digit//10
print("Number of digits in",x,"is",count)
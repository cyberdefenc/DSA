

x=int(input("Enter a number: "))
arm=0
digit=x
count=len(str(x))
while digit>0:
    rev=digit%10
    pw=rev**count
    arm+=pw
    digit=digit//10
if arm==x:
    print("The number ",x," is an armstrong number")
else:
    print("The number ",x," is not an armstrong number")
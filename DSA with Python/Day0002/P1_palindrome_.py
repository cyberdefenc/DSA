x=int(input("Enter a number: "))
rev=0
digit=x
while digit>0:
    rev=rev*10+digit%10
    digit=digit//10
if rev==x:
    print("The number ",x," is a palindrome")
else:
    print("The number ",x," is not a palindrome")

#Since division by 10 so time complexity is O(log n)

#Space complexity is O(1) since we are using only a few variables
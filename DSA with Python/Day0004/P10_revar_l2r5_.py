num=[2,4,1,7,6,3,8,9,5]
print("Original Array:", num)

def revarr(num,left,right):
    if left>=right:
        return
    num[left],num[right]=num[right],num[left]
    revarr(num,left+1,right-1)

revarr(num,2,5)
print("Reversed array",num)
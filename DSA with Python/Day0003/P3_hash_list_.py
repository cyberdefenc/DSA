n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

hash_list=[0]*11 # Initialize a list of size 11 with zeros

for i in n:
    hash_list[i]+=1

for j in m:
    if j<1 or j>10:
        print(0)
    else:
        print(hash_list[j])
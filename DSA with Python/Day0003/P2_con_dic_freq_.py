
print("Enter you elements that most of occur recursively")
list=[]
while True:
    try:
        n = int(input("Enter a number : "))
        list.append(n)
    except ValueError:
        if input("Type 'done' to finish or press Enter to continue: ").lower() == 'done':
            break
        else:
            print("Invalid input, please enter a number.")
# Hashing
print("Frequency of elements in the list: (Storing in dictionary) which is called Hashing")
hash_map=dict() # or {}
for i in range(0,len(list)):
    hash_map[list[i]]=hash_map.get(list[i],0)+1
print(hash_map)


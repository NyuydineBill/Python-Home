size=int(input("whats the array sizee\n"))
array=[]
for i in range(size):
    items=input("enter the items")
    array.append(items)
    print(items)
    reverse=[]
print("the reversed array is:")
for i in range(len(array)-1,-1,-1):
    reverse.append(array[i])
    print(reverse)

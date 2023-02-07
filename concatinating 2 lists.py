
l1=[]
size=int(input("enter size of array\n"))

for i in range(size):

    value=int(input("enter elements of first array\n"))
    l1.append(value)
l2=[]

for i in range(size):
    value=int(input("enter elements of second array\n"))
    l2.append(value)

def merge(l1,l2):
    merge=l1+l2
    return merge
print(merge(l1,l2))


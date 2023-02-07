
size=int(input("enter size of array\n"))
l1=[]
for i in range(size):

    value=int(input("enter elements of first array\n"))
    l1.append(value)
l2=[]
for i in range(size):
    value=int(input("enter elements of second array\n"))
    l2.append(value)
def compare(l1,l2):
    diff1=list(set(l1) -set(l2))
    diff2=list(set(l2) -set(l1))
    actual_diff=diff1+diff2
    return actual_diff
print("the different terms are:",compare(l1,l2))

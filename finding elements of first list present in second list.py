
def findmissing(size,l1,l2):
    for i in range(size):
        for j in range(size):
            if(l1[i]==l2[j]):
                break
        if (j == size-1):
            print(l1[i],end=" ")
if __name__ =="__main__":
    size=int(input("enter size of array\n"))
    l1=[]
    for i in range(size):

        value=int(input("enter elements of first array\n"))
        l1.append(value)
    l2=[]
    for i in range(size):
        value=int(input("enter elements of second array\n"))
        l2.append(value)
    print(findmissing(size,l1,l2),"is in second list")

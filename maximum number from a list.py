array=[]
size=int(input("please enter number of elements\n"))
for i in range(size):
    mylist=input("enter the numbers\n")
    array.append(mylist)
print("maximum number from list is",max(array))

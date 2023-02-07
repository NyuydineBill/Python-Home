list=[]
number=int(input("enter number off elemnts\n"))
for i in range(1,number+1):
    value=int(input("enter the numbers"))
    list.append(value)
print("\n positive numbers are :")
for j in range(number):
    if(list[j]>=0):
        print(list[j],"\n",end='')

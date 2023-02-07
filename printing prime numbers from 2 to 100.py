n=100
print("the prime  numberss from 1 to 100 are : \n")
for x in range(2,n+1):
    count=0
    for i in range(2,(x//2+1)):
        if(x%i==0):
            count+=1
            break
    if(count==0 and x!=1):
        print(" %d"%x,end=" ")

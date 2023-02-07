num=int(input("how many numbers\n"))
sum=0
for n in range(num):
    numbers=eval(input("ENTER ANY NUMBER"))
    sum+=numbers
average=sum/num

print(average)

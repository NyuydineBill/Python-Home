number=int(input('enter any number\n'))
sum=0

while(number>0):
    remainder=number%10
    sum=sum+remainder
    number=number//10
print('the sum of the digits is',sum)

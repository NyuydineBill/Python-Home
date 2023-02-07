def fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
       return fibo(n-1) + fibo(n-2)
number = int(input("enter number to find its fibonocci\n"))
list=[str(fibo(i)) for i in range(0,number+1)]

print(','.join(list))

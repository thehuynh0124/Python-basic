n = int(input())
temp =int
for i in range(2, n):
    temp = 0
    while (n % i == 0):
        temp = temp + 1
        n = n / i
    if(temp):
        print (i,end = "")
        if(temp >1 ):
            print("^",temp,end = "")
        if(n>i):
            print("*",end = "")
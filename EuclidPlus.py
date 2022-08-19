print ("nhap a: ")
a = int(input())
print("nhap b: ")
b = int(input())
x = int(1)
y = int(0)
u = int(0)
v = int(1)
if b == 0:
    exit
while b != 0:
    x = s = t = q = r = int()
    q = a/b
    r = a-b*q
    s = x-u*q
    t = y-v*q
    a=b
    x=u
    y=v
    b=r
    u=s
    v=t
print("a = ", a,"x = ", x,"y = ", y)





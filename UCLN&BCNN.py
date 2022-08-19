#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = []
#nhập số lượng các số cần tính
a = int(input("nhap so luong cac so can tinh "))
print("nhap lan luot cac so can tinh")
for i in range(0, a):
    n = int(input())        
    lst.append(n)
#####
def UCLN(a, b):
    if b == 0:
        return a
    else:  # b != 0
        return UCLN(b, a % b)
####
def BCNN(a, b):
    return a*b / UCLN(a, b)
####
b = lst[0]
c = lst[0]
for j in range(1,len(lst)):
    s=UCLN(b,lst[j])
    p=BCNN(c, lst[j])
    b=s
    c=p
print("UCLN cua cac so tren la ", b)
print("BCNN cua cac so tren la ", c)


# In[ ]:





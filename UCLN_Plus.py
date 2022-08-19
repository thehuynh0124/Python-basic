#!/usr/bin/env python
# coding: utf-8

# In[35]:


lst = []
#nhập số lượng các số cần tính
a = int(input("nhap so luong cac so can tinh "))
print("nhap lan luot cac so can tinh")
for i in range(0, a):
    n = int(input())        
    lst.append(n) # adding the element
def UCLN(a, b):
    while b != 0:
        r = int(a%b)
        a = b
        b = r
    return a
b = lst[0]
for j in range(1,len(lst)):
    s=UCLN(b,lst[j])
    b=s
print("UCLN cua cac so tren la", b)
    


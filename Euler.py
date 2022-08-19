#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input("Nhập số nguyên dương n = "))
def eulerphi(n):
    if(n == 0):
        return 0
    result = int(n)
    for i in range(2, n):
        if (n % i == 0):
            result = result - result/i
            while (n % i == 0):
                n = n/i
    if (n > 1):
        result = result - result/n
    return int(result)
print("phi",n ,"=", eulerphi(n))


# In[ ]:





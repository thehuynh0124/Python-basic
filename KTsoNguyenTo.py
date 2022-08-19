#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print("moi nhap a: ")
a = int(input())
def songuyento(a):
    b = int(math.sqrt(a))
    if a <2:
        return False
    for i in range(2,(b+1)):
        if a % i ==0:
            return False
            break
        else:
            return True
if songuyento(a) == False:
    print(a, "khong phai la so nguyen to")
else:
    print(a, "la so nguyen to")
    


# In[ ]:





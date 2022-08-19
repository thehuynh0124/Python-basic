#!/usr/bin/env python
# coding: utf-8

# In[18]:


n = int(input("Nhập số nguyên dương n = "))
def phanTichSoNguyen(n):
    i = 2;
    listNumbers = []
    while (n > 1):
        if (n % i == 0):# nếu n chia i dư 0
            n = int(n / i)
            listNumbers.append(i)# lấy i vào chuỗi kết quả
        else:
            i = i + 1;
    if (len(listNumbers) == 0): #nếu chuỗi kq rỗng
        listNumbers.append(n) #thêm n vào chuỗi kq(n là số nguyên tố)
    return listNumbers

listNumbers = phanTichSoNguyen(n)
size = len(listNumbers)
sb = ""
for j in range(0, size - 1):
    sb = sb + str(listNumbers[j]) + " x "
sb = sb + str(listNumbers[size-1])
print(n, "=", sb)


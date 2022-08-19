#!/usr/bin/env python
# coding: utf-8

# In[34]:


n = int(input("Nhập số cần chuyển = "))
a = int(input("Nhập hệ cơ số ban đầu = "))
b = int(input("Nhập hệ cơ số cần chuyển = "))
##hệ 10 sang bất kỳ
def convert_number_10_to_b(n, b):
    if (n < 0 or b < 2 or b > 16):
        return ""
 
    sb = ""
    m = 0;
    remainder = n
 
    while (remainder > 0):
        if (b > 10):
            m = remainder % b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb)); # đảo ngược chuỗi sb
## hệ bất kỳ sang 10
def convert_number_b_to_10(n):  
    decimal, i = 0, 0
    while(n != 0):
        dec = n % 10
        decimal = decimal + dec * pow(a, i)
        n = n//10
        i += 1
    return decimal 
def convert_number(n, b):
    result = convert_number_b_to_10(n)
    result = convert_number_10_to_b(result, b)
    return result
if (a == 10):
    print("Hệ cơ số", b, "của", n, "là:", convert_number_10_to_b(n, b))
if (a != 10 and b == 10):
    print("Hệ cơ số", b, "của số nguyên ", n, "là:", convert_number_b_to_10(n))
else:
    print("Hệ cơ số", b, "của số nguyên ", n, "là:", convert_number(n,b))


# In[ ]:





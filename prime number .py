#!/usr/bin/env python
# coding: utf-8

# In[6]:


num=int(input('enter a  number'))
flag=False
if num==1:
    print('1 is not a prime number')
for i in range(2,num):
    if num%i==0:
        flag=True
if flag:
    print(num,'is not a prime number')
else:
    print(num ,'is a prime number')
    


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


def facto(num):
    if num ==0 or num==1:
        return 1
    else:
        return num*facto(num-1)
    
    
    
num=int(input('enter a number'))
print(facto(num))


# In[ ]:





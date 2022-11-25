#!/usr/bin/env python
# coding: utf-8

# In[2]:


def findsum(n):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
    
num=int(input('enter  the numbers upto which you have to find the sum'))
print('the sum is ---',findsum(num))


# In[ ]:





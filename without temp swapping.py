#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swaptwonumbers(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print('num1=',num1,'num2=',num2)

a=int(input('enter num1---'))
b=int(input('enter num2--'))
swaptwonumbers(a,b)


# In[ ]:





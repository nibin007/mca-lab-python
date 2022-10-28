#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath
a=int(input("enter the first number "))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=(b**2)-4*a*c
sqrroot=cmath.sqrt(d)
sol1=(-b+sqrroot)/2*a
sol2=(-b-sqrroot)/2*a
print('the first root is {},the second root is {}'.format(sol1,sol2))


# In[ ]:





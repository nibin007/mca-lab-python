#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input('enter the year'))
if a%400==0:
    print(a,'is a leapyear')
elif a%4==0 and a%100!=0:
    print(a,'is a leap year')
else:
    print(a, 'is not a leapyear')


# In[ ]:





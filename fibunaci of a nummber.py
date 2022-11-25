#!/usr/bin/env python
# coding: utf-8

# In[11]:


def fibonaci(n):
    a = 0
    b = 1
     
    if n < 0:
        print("Incorrect input")
         
    
    elif n == 0:
        return 0
       
    
    elif n == 1:
        return b
    else:
        while a<=n:
            print(a)
            c=a+b
            b=a
            a=c
           
 
num=int(input('enter the number to find fibonacci series of the same--'))
fibonaci(num)


# In[ ]:





# In[ ]:





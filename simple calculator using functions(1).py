#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sum(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def mult(a,b):
    return a*b
def division(a,b):
    if b==0:
        return 'zero division not possible'
    else:
        return float(a/b)
    
num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
print('''1.ADD 
         2.SUBTRACT
         3.MULTIPLICATION
         4.DIVISION


''')
choice=int(input('\n enter the choice'))
if(choice==1):
    print('addition of ',num1,'and',num2,'is', sum(num1,num2))
    

elif(choice==2):
    print('subtraction of ',num1,'and',num2,'is', subtraction(num1,num2))
elif(choice==3):
    print('multiplication of ',num1,'and',num2,'is', mult(num1,num2))
elif(choice==4):
    print('division of ',num1,'and',num2,'is', division(num1,num2))
else:
    print('incorrect choice')
    


# In[ ]:





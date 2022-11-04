#!/usr/bin/env python
# coding: utf-8

# In[7]:


num1=int(input('enter the first number \n'))
num2=int(input('enter the second number \n'))
print('enter the options to choose operations')
print('''1.addition \n
        2.substraction \n
        3.multiplication \n
        4.division \n

''')
choice=int(input())

if (choice==1):
       print('addition of ',num1,'and',num2,'is',num1+num2)

elif (choice==2):
        print('subtraction of',num1, 'and',num2,'is',num1-num2)
     
             

elif (choice==3):
        print('multiplication of',num1,'and',num2,'is',num1*num2)
 
    
elif (choice==4):
   
                if num2==0:
                       print('zero division not possible')
                else:
                       print('division of',num1 ,'and', num2 ,'is' ,float(num1/num2))
   
else:
      print('invalid option')
           


# In[ ]:





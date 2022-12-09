#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter no of students: "))
studlist=[]
for i in range(0,n):
    stud={}
    stud['Name']=input("Enter Name : ")
    stud['Roll No']=int(input("Enter Roll No : "))
    studlist.append(stud)
print("Name And Roll No: ")
print()
for i in range(0,n):
    print(studlist[i])


# In[ ]:





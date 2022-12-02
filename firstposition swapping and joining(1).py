#!/usr/bin/env python
# coding: utf-8

# In[2]:


def change(text1,text2):
    first=text1[1]
    second=text2[1]
    a=list(text1)
    b=list(text2)
    a[1]=second
    b[1]=first
    string1=''.join(a)
    string2=''.join(b)
    final=string1+' '+string2
    return final
    
    
    
word1=input('enter the first word')
word2=input('enter the second word')
print("joined word with swapping letters in first position is ",change(word1,word2))


# In[ ]:





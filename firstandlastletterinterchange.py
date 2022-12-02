#!/usr/bin/env python
# coding: utf-8

# In[4]:


def interchange(letter):
    firstletter=letter[0]
    lastletter=letter[-1]
    new=list(letter)
    new[0]=lastletter
    new[-1]=firstletter
    final=''.join(new)
    return final

word=input("enter the Word to interchange")
print("interchanged word is ",interchange(word))


# In[ ]:





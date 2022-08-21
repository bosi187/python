#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=1
result=1

while i <= 100:
    result *= i
    if i == 42:
        print('magic number 42 reached ! stooping execution..') 
        break      
    i += 1      
print("i:",i)
print("result",result)  


# In[ ]:





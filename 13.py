#!/usr/bin/env python
# coding: utf-8

# In[1]:


#increasing and decreasing of stars
line='*'
max_lenght=10

while len(line) <= max_lenght:
    print(line)
    line+="*"
while len(line) > 0:
    print(line)
    line=line[:-1]


# In[ ]:





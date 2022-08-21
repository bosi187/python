#!/usr/bin/env python
# coding: utf-8

# In[1]:


#multiplying with even numbers.
i=1
result=1

while i < 20:
    i += 1
    if i % 2 !=0:
        print("skipping {}".format(i)) 
        continue
    print("multiplying with {}".format(i))
    result=result*i
          
print("i:",i)
print("result",result)


# In[ ]:





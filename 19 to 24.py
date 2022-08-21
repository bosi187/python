#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


arr1=list(range(1000))
arr2=list(range(1000,2000))

arr1_np = np.array(arr1)
arr2_np = np.array(arr2)


# In[6]:


get_ipython().run_cell_magic('time', '', 'result = 0\nfor x1 ,x2 in zip(arr1,arr2):\n    result += x1*x2\nresult    \n    ')


# In[7]:


get_ipython().run_cell_magic('time', '', 'np.dot(arr1_np,arr2_np)')


# In[9]:


climate_data = np.array([[73,67,43],
                        [91,88,64],
                        [87,134,58],
                        [102,43,37],
                        [69,96,70]])


# In[10]:


climate_data


# In[11]:


climate_data.shape


# In[23]:


w1,w2,w3=0.3,0.2,0.5


# In[25]:


weights=np.array([w1,w2,w3])


# In[26]:


weights


# In[27]:


weights.shape


# In[28]:


arr2 = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,1,2,3]])


# In[29]:


arr3= np.array([[11,12,13,14],
               [15,16,17,18],
               [19,11,12,13]])


# In[30]:


# adding a sclar
arr2+3


# In[31]:


# element-wise subtraction
arr3 - arr2


# In[32]:


# element-wise adding
arr2 + arr3


# In[33]:


# Division by scalar
arr2/2


# In[34]:


# element-wise multiplication
arr2*arr3


# In[36]:


# modulus with scalar
arr2 % 4


# In[ ]:





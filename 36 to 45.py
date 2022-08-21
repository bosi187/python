#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


data = np.arange(10)


# In[4]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.plot(data)


# In[5]:


plt.title("interactive test")


# In[6]:


plt.xlabel("sample name")


# In[7]:


plt.ylabel("sample value")


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


x=[1,2,3,4]
y=[1,4,9,16]

plt.plot(x,y)


# In[10]:


d=np.arange(0.,5.,0.2)


# In[11]:


plt.plot(d, d,'r--',d,d**2,'bs',d,d**3,'g^')


# In[12]:


plt.savefig('my-graph.png')


# In[13]:


plt.savefig('my-graph-2.png',
            dpi=400, bbox_inches='tight')


# In[14]:


fig=plt.figure()


# In[15]:


ax1 = fig.add_subplot(2, 2, 1)


# In[16]:


ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)


# In[17]:


data=np.random.randn(50,).cumsum() 


# In[18]:


ax1.plot(data, 'k--')


# In[19]:


ax2.plot(data, "r-")
ax3.plot(data, "b.")


# In[20]:


x=[1,2,3,4,5]
y=[10,11,12,13,14]


# In[21]:


fig=plt.figure()


# In[22]:


fig=plt.figure()
ax=fig.add_subplot(1,1,1)


# In[23]:


ax.plot(x, y, 'r--')


# In[24]:


ax.plot(x, y, linestyle='--', color='r')


# In[25]:


get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[26]:


plt.plot(data, 'ko--')


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


plt.plot(data, 'k--', label='Default')


# In[29]:


plt.plot(data, 
         'k-', 
         drawstyle='steps-post', 
         label='Stepwise')


# In[30]:


plt.plot(data, 'k-', 
         drawstyle='steps-post', 
         label='Stepwise')
plt.legend(loc='best')


# In[40]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[41]:


fig=plt.figure()


# In[42]:


ax = fig.add_subplot(1, 1, 1)


# In[43]:


ax.plot(data)


# In[44]:


location=ax.set_xticks([0,10,20,30,40,50])
label=ax.set_xticklabels(
    ["one","two","three","four","five","six"],
    rotation=30,
    fontsize="small")


# In[45]:


ax.set_title('First Graph')


# In[46]:


ax.set_xlabel('Stages')
ax.set_ylabel('Anything')


# In[47]:


feature={"title":"Perfect Graph", 
         "xlabel":"Steps", 
         "ylabel":"Numbers"}


# In[48]:


ax.set(**feature)


# In[50]:


fig=plt.figure()


# In[51]:


ax=fig.add_subplot(1,1,1)


# In[52]:


data1=np.random.randn(1000).cumsum()
data2=np.random.randn(1000).cumsum()
data3=np.random.randn(1000).cumsum()


# In[59]:


ax.plot(data1, 'k', label='one')
ax.plot(data2, 'b--', label='two')
ax.plot(data3, 'r.', label='three')


# In[60]:


ax.legend()


# In[61]:


import pandas as pd


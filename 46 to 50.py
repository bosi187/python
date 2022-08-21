#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


plt.style.use('classic')


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


rng = np.random.RandomState(0)


# In[5]:


x = np.linspace(0, 10, 250)


# In[6]:


y = np.cumsum(rng.randn(250, 6), 0)


# In[7]:


plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='best')


# In[8]:


get_ipython().system('pip install seaborn')


# In[9]:


import seaborn as sns


# In[10]:


sns.set()


# In[11]:


plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')


# In[12]:


iris = sns.load_dataset("iris")


# In[13]:


iris.head()


# In[14]:


setosa=iris.loc[iris.species== "setosa"]
virginica = iris.loc[iris.species == "virginica"]


# In[15]:


setosa.sepal_length.plot.hist()


# In[16]:


sns.kdeplot(setosa.sepal_length, shade=True, color="r")


# In[17]:


sns.histplot(iris.sepal_length, kde=True)


# In[18]:


sns.histplot(iris.sepal_length, kde=True, color="r")
sns.histplot(iris.sepal_width, kde=True,color="b")


# In[19]:


sns.kdeplot(data=iris, x="sepal_length", y="sepal_width")


# In[20]:


sns.kdeplot(
    data=iris, x="sepal_length", 
    y="sepal_width", shade=True)


# In[21]:


with sns.axes_style('white'):
    sns.jointplot(
        data= iris, x="sepal_length", 
        y="sepal_width", kind='kde')


# In[22]:


with sns.axes_style('white'):
    sns.jointplot(
        data= iris, x="sepal_length", 
        y="sepal_width", kind='hex')


# In[23]:


sns.pairplot(iris, hue='species')


# In[24]:


tips=sns.load_dataset('tips')


# In[25]:


tips.head()


# In[26]:


tips["tip_percent"]=tips[
    "tip"]*100/tips["total_bill"]


# In[27]:


grid=sns.FacetGrid(
    tips, row="smoker",col="time", 
    margin_titles=True)


# In[28]:


grid.map(
    plt.hist, "tip_percent", 
    bins=np.linspace(0,40,15))


# In[29]:


with sns.axes_style(style='ticks'): 
    g = sns.catplot(x="day", y="total_bill", 
                    data=tips, kind="box")
g.set_axis_labels("Day", "Total Account")


# In[30]:


sns.jointplot(x="total_bill", 
              y="tip", 
              data=tips, 
              kind='reg')


# In[31]:


with sns.axes_style('white'):
	g = sns.catplot(x="size", data=tips, 
                    aspect=2,kind="count", color='steelblue') 	
	g.set_xticklabels(step=5)


# In[32]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[34]:


iris = sns.load_dataset("iris")


# In[35]:


iris.head()


# In[36]:


iris.petal_length.plot()


# In[37]:


iris.plot()


# In[38]:


data = pd.Series(np.random.rand(5), index=list('abcde'))


# In[39]:


data


# In[40]:


data.plot.bar(color='b', alpha=1)


# In[41]:


data.plot.barh(color='r', alpha=0.5)


# In[42]:


df =pd.DataFrame(np.random.rand(5, 3),index=['one', 'two', 'three', 'four', 'five'], 
                 columns=pd.Index(list("ABC")))


# In[43]:


df.head()


# In[44]:


df.plot.bar()


# In[45]:


df.plot.barh(stacked=True, alpha=1)


# In[46]:


tips=sns.load_dataset('tips')


# In[47]:


tips.head()


# In[48]:


day_size=pd.crosstab(tips["day"],tips["size"])
day_size


# In[49]:


day_size.plot.bar()


# In[50]:


tips['tips_perc'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
tips.head()


# In[51]:


sns.barplot(x='day', y='tips_perc', data=tips, orient='v')


# In[52]:


sns.barplot(x='day', y='tips_perc', hue='time', data=tips, orient='v')


# In[53]:


tips['tips_perc'].plot.hist(bins=70)


# In[54]:


sns.histplot(tips['tips_perc'], kde=True, bins=50, color="r")


# In[55]:


sns.regplot(x='sepal_length', y='petal_length', data=iris)


# In[56]:


sns.pairplot(iris)


# In[57]:


sns.pairplot(iris,hue="species")


# In[58]:


tips.head()


# In[59]:


sns.catplot(x='day', y='tips_perc', hue='time', col='smoker', kind='bar', data=tips)


# In[60]:


sns.catplot(x='day', y='tips_perc', row='time',col='smoker',kind='bar', data=tips)


# In[61]:


sns.catplot(x='day', y='tips_perc', row='time',col='smoker',kind='box', data=tips)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


from urllib.request import urlretrieve


# In[4]:


italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')


# In[5]:


get_ipython().system('pip install pandas --upgrade --quiet')


# In[6]:


import pandas as pd


# In[7]:


covid_df=pd.read_csv('italy-covid-daywise.csv')


# In[8]:


covid_df.info()


# In[9]:


covid_df.columns


# In[10]:


covid_df.shape


# In[11]:


#pandas format is simliar to this
covid_data_dict = {
    'date':       [ '2020-08-30','2020-08-31','2020-09-01','2020-09-02','2020-09-03'],
    'new_cases':  [ 1444,1365,996,975,1326],
    'new_deaths': [1,4,6,8,6],
    'new_tests':  [53541,42583,54395,None,None]
}


# In[12]:


covid_data_dict['new_cases']


# In[13]:


covid_df['new_cases']


# In[14]:


type(covid_df['new_cases'])


# In[15]:


covid_df['new_cases'][246]


# In[16]:


covid_df['new_tests'][240]


# In[17]:


covid_df.at[246,'new_cases']


# In[18]:


covid_df.at[240,'new_tests']


# In[19]:


cases_df = covid_df[['date','new_cases']]
covid_df


# In[20]:


covid_df.loc[243]


# In[21]:


type(covid_df.loc[243])


# In[22]:


covid_df.head()


# In[23]:


covid_df.tail()


# In[27]:


covid_df.tail(10)


# In[28]:


covid_df.head(3)


# In[29]:


covid_df.at[0,'new_tests']


# In[30]:


type(covid_df.at[0,'new_tests'])


# In[31]:


covid_df.loc[108:113]


# In[32]:


covid_df.sample(5)


# In[ ]:





# In[33]:


#analye data from the data frames
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()


# In[34]:


print(' The number of repoeted nem cases is {} and the number of reported deaths {}'.format(int(total_cases),(total_deaths)))


# In[35]:


total_cases=covid_df['new_cases'].sum()
print('The total number of new cases is {}'.format(int(total_cases)))


# In[36]:


death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()


# In[37]:


print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))


# In[38]:


initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()


# In[39]:


total_tests


# In[40]:


positive_rate = total_cases / total_tests


# In[41]:


print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate*100))


# In[ ]:





# In[ ]:





# In[44]:


high_new_cases = covid_df.new_cases > 1000


# In[45]:


high_new_cases


# In[46]:


covid_df[high_new_cases]


# In[47]:


high_cases_df = covid_df[covid_df.new_cases > 1000]


# In[48]:


high_cases_df


# In[49]:


from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])


# In[50]:


positive_rate


# In[51]:


high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]


# In[52]:


high_ratio_df


# In[53]:


covid_df.new_cases / covid_df.new_tests


# In[54]:


covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests


# In[55]:


covid_df


# In[56]:


covid_df.drop(columns=['positive_rate'], inplace=True)


# In[57]:


covid_df.sort_values('new_cases', ascending=False).head(10)


# In[58]:


covid_df.sort_values('new_deaths', ascending=False).head(10)


# In[59]:


covid_df.sort_values('new_cases').head(10)


# In[60]:


covid_df.loc[169:175]


# In[61]:


covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2


# In[63]:


covid_df.date


# In[64]:


covid_df['date'] = pd.to_datetime(covid_df.date)


# In[65]:


covid_df['date']


# In[66]:


covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
covid_df


# In[67]:


# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]

# Extract the subset of columns to be aggregated
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()


# In[68]:


covid_may_totals


# In[69]:


type(covid_may_totals)


# In[70]:


covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()


# In[71]:


# Overall average
covid_df.new_cases.mean()


# In[72]:


# Average for Sundays
covid_df[covid_df.weekday == 6].new_cases.mean()


# In[73]:


covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()


# In[74]:


covid_month_df


# In[75]:


covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
covid_month_mean_df


# In[76]:


covid_df['total_cases'] = covid_df.new_cases.cumsum()


# In[77]:


covid_df['total_deaths'] = covid_df.new_deaths.cumsum()


# In[78]:


covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests


# In[79]:


covid_df


# In[80]:


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')


# In[81]:


locations_df = pd.read_csv('locations.csv')


# In[82]:


locations_df


# In[83]:


locations_df[locations_df.location == "Italy"]


# In[84]:


covid_df['location'] = "Italy"
covid_df


# In[85]:


merged_df = covid_df.merge(locations_df, on="location")
merged_df


# In[86]:


merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population


# In[87]:


merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population


# In[88]:


merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population


# In[89]:


merged_df


# In[90]:


result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]


# In[91]:


result_df


# In[92]:


result_df.to_csv('results.csv', index=None)


# In[93]:


result_df.new_cases.plot();


# In[94]:


result_df.set_index('date', inplace=True)
result_df


# In[95]:


result_df.loc['2020-09-01']


# In[96]:


result_df.new_cases.plot()
result_df.new_deaths.plot();


# In[97]:


result_df.total_cases.plot()
result_df.total_deaths.plot();


# In[98]:


death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title='Death Rate');


# In[99]:


positive_rates = result_df.total_cases / result_df.total_tests
positive_rates.plot(title='Positive Rate');


# In[100]:


covid_month_df.new_cases.plot(kind='bar');


# In[101]:


covid_month_df.new_tests.plot(kind='bar')


# In[ ]:





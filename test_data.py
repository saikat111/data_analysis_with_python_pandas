#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('NationalNames.csv')


# In[73]:


print(data)


# In[13]:


print (data[0:5]['Year'])


# In[15]:


print (data['Year']==2014)


# In[19]:


print (data.loc[:,['Name','Year']])


# In[27]:


print(data.loc[:,["Gender","Year"]])


# In[34]:


print(data.loc[data["Gender"] == 'F'])


# In[35]:


print(data.loc[data["Year"] == 2014])


# In[38]:


print(data.sort_values('Name'))


# In[39]:


data.sort_values('Name')


# In[40]:


data.sort_values('Year')


# In[41]:


data.sort_values('Year').head(5)


# In[60]:


data.loc[data['Year']==2014].head(5)


# In[61]:


data.loc[data['Name']== 'Mary']


# In[74]:


data.loc[(data['Name']== 'Mary') & (data['Year']== 2014)]


# In[76]:


data.loc[(data['Name']== 'Mary') & (data['Year']== 2014) & (data['Gender']== 'F')]


# In[79]:


data.loc[(data['Name']== 'Mary') & (data['Year']== 2014) & (data['Gender']== 'M')]


# In[ ]:





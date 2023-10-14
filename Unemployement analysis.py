#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'C:\Users\nitip\OneDrive\Desktop\Data Science Project\Unemployment in India.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


x=df['Region']


# In[9]:


x


# In[10]:


y=df[' Estimated Unemployment Rate (%)']


# In[11]:


y


# In[12]:


df2=df.iloc[:,3]


# In[13]:


df2


# In[14]:


fg=px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[15]:


fg=px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[16]:


fg=px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Scatter Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[17]:


fg=px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[ ]:





# In[ ]:





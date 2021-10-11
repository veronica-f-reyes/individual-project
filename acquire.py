#!/usr/bin/env python
# coding: utf-8

# #### Individual Class Project
# 
# ## Predicting Major League Baseball Game Outcomes
# ***
# ### Acquire Major League Baseball Data from baseball-reference.com
# 
# - All data is acquired from batting game logs for all 30 Major League Baseball teams for the year 2021
# - All batting logs were combined into one .csv file
# - Data source is baseball-reference.com

# In[1]:


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np


# In[3]:


#Read local .csv downloaded and combined from 2021 batting logs for all 30 Major League Baseball teams 
#from baseball-reference.com and store data in a dataframe
df = pd.read_csv('sportsref_download.csv')
df.info()


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


#Function to get baseball batting log data

def get_batting_log_data():
    df = pd.read_csv('sportsref_download.csv')
    
    return df
    


# In[ ]:





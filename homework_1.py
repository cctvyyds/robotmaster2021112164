#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
path="data_20220918210128.csv"


# In[3]:


X = np.loadtxt(path, delimiter=",", dtype="float",usecols = (0,1,2))


# In[4]:


y=np.loadtxt(path, delimiter=",", dtype="float",usecols = (3))


# In[6]:


W = np.linalg.inv(X.T@X)@X.T@y


# In[7]:


print(W)


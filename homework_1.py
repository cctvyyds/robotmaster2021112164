#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
path="data_20220918210128.csv"


# In[4]:


X = np.loadtxt(path, delimiter=",", dtype="float",usecols = (0,1,2))
x0=np.ones(X.shape[0])
X=np.insert(X,3,x0,axis=1)


# In[6]:


y=np.loadtxt(path, delimiter=",", dtype="float",usecols = (3))


# In[7]:


W = np.linalg.inv(X.T@X)@X.T@y


# In[8]:


print(W)


# In[ ]:





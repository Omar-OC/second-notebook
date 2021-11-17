#!/usr/bin/env python
# coding: utf-8

# In[1]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]


# In[16]:


# task: use a list comprehension to create the output y values
# note how we can't simply write y = m*x + c
# one line of code here:
#y = [m * for val in x + c]

y = [m*val+c for val in x]


# In[17]:


print(y)


# In[7]:


# task: import numpy
# one line of code here:
import numpy as np


# In[8]:


X = np.array(x)
Y = m*X + c


# In[9]:


print(Y)


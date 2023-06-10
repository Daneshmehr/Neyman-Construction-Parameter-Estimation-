#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
 
def func(x):
    x = (x/2)**2 - 4
    return x
 
x = np.arange(-2, 2, 0.01)
y = func(x)

plt.title("Minimum of the function")
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()  
 
x0 = -1
result = minimize(func,  x0, method="nelder-mead")
print(result)


# In[ ]:





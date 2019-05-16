# -*- coding: utf-8 -*-
"""
Spyder Editor
plt.plot() ve plt.scatter() arasındaki fark
"""
import numpy as np
import matplotlib.pyplot as plt


# Create data
x = np.array([1,2,3,4,5])
y = np.array([3,4,5,6,7])


plt.subplot(2,2,1)
plt.plot(x,y)


plt.subplot(2,2,3)
plt.scatter(x,y)
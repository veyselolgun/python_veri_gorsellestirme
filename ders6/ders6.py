#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 00:00:47 2019

"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(2,10,1)
y=np.arange(3,18,2)

plt.plot(x,y)

""" 
x ve y kordinatında aralıkları sadece 1 olacak şekilde ayarladık
plt.xticks() ve plt.yticks() ile. Eğer aralıklar 3'er olarak  artsın istersek
plt.xticks(np.arange(1,10,3)) yazarız
"""

plt.xticks(np.arange(1,10))
plt.yticks(np.arange(1,18))
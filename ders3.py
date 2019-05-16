#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:13:37 2019

@author: veysel
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6])
y=np.array([3,5,6,9,11,14])

plt.xlabel("X ekseni")
plt.ylabel("Y ekseni")
plt.title("ders3 grafik")
plt.plot(x,y,color="blue",marker="*", markerfacecolor='red', markersize=12)

plt.show()


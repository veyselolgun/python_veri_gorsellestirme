#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:34:06 2019

@author: veysel
"""


import numpy as np
import matplotlib.pyplot as plt

#create data

x=np.array([1,2,3,4,5])
kare=np.array([x[0]**2,x[1]**2,x[2]**2,x[3]**2,x[4]**2])
kup=np.array([x[0]**3,x[1]**3,x[2]**3,x[3]**3,x[4]**3])
fourth=np.array([x[0]**4,x[1]**4,x[2]**4,x[3]**4,x[4]**4])



plt.plot(x,kare,"blue",label="karesi",marker=".",markerfacecolor="yellow",markersize=12)

plt.plot(x,kup,"yellow",label="küpü",marker=".",markerfacecolor="red",markersize=12)

plt.plot(x,fourth,"red",label="4. kuvveti",marker=".",markerfacecolor="cyan",markersize=12)

plt.legend()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:00:32 2019

"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,6)
y=np.arange(2,11,2)


"""subplot(2,2,1) ile 2 satır 2 sütundan oluşan bir bölge oluşturduk
ve 1. bölgeye ilk grefiğimizi yerleştirdik"""
plt.subplot(2,2,1)
plt.plot(x,y,"red",linewidth=2)


plt.subplot(2,2,2)
plt.plot(y,x,"blue",linewidth=2)


"""burada ise 3. bölgeye grafiğimizi(ikinci dereceden) yerleştirdik"""
plt.subplot(2,2,3)
plt.plot(x,y*y,"black",linewidth=2)


plt.subplot(2,2,4)
plt.plot(x,y*y*y,"yellow",linewidth=2)
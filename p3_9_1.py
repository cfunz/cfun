# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:20:07 2016

@author: Clark
"""

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt
x=np.linspace(-1,5,1000)
m=1000
sample=uniform.rvs(loc=0,scale=4,size=m,random_state=None) 
pdf1=uniform.pdf(x,loc=0,scale=4)

plt.close("all")
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x,pdf1)
plt.title("PDF")
plt.subplot(2,1,2)
plt.hist(sample, bins=12,range=(-1,5))  # plt.hist passes it's arguments to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()

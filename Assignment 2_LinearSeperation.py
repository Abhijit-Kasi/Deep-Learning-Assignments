# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:24:52 2021

@author: abhij
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.array([1,1,2,3,3,6,6,6,9,9,10,11,12,13,16,18])
y = np.array([18,13,9,6,15,11,6,3,5,2,10,5,6,1,3,1])
label = np.array([1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1])

plt.scatter(x, y, c=label, s=60)
plt.show()

def mapping(x, y): 
    xx=np.c_[(x,y)]
    x_1 = xx[:,0]**2        
    x_2 = np.sqrt(2)*xx[:,0]*xx[:,1]        
    x_3 = xx[:,1]**2	
    trans_x = np.array([x_1, x_2, x_3])				
    return trans_x

x_1  = mapping(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_1[0], x_1[1], x_1[2], c=label, s=60)
ax.view_init(30, 185)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()	
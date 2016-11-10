# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:30:10 2016

@author: nguyenv7
"""
import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt

filename = "dumpMid0.pkl"
with open(filename, 'rb') as infile:
    midData = pickle.load(infile)
    
x=midData[0]
tilde_x=midData[1]
y = midData[2]
z = midData[3]

sID = 2;
#%%
imgX = x[sID,:]
imgX = np.reshape(imgX,[28,28])
plt.imshow(imgX, cmap='gray')
plt.savefig('X.png')
#%%
imgXT = tilde_x[sID,:]
imgXT = np.reshape(imgXT,[28,28])
plt.imshow(imgXT, cmap='gray')
plt.savefig('Xtil.png')

#%%
imgZ = z[sID,:]
imgZ = np.reshape(imgZ,[28,28])
plt.imshow(imgZ, cmap='gray')
plt.savefig('Z.png')
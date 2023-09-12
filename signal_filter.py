#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def myFFT(v):
    n = len(v)
    
    if n==1:
        return v
    else:
        # implement some recursive
        F_even = myFFT(v[::2])
        F_odd = myFFT(v[1::2])
        
        # frequency factor
        fac = np.exp(-2j*np.pi*np.arange(n)/n)
        
        # build FFT array
        F = np.concatenate([
            F_even + fac[:int(n/2)]*F_odd,
            F_even + fac[int(n/2):]*F_odd
            ])
        
        return F

# ID
print("Nama: Achmadi ST MT")
print("NRP: 2410100085")

# X array linear spacing
X = np.arange(0,1,1.0/128)

# Y sinus function
Y = np.sin(2*np.pi*X)

# create noise array at X length
R = np.random.rand(len(X))

# add noise to sine result
Yr = Y + R

# FFT all
FY = np.abs(myFFT(Y))
FYr = np.abs(myFFT(Yr))

# plot all
fig, ax = plt.subplots(2,2)
ax[0,0].plot(X,Y)
ax[0,1].plot(FY)
ax[1,0].plot(X,Yr)
ax[1,1].plot(FYr)
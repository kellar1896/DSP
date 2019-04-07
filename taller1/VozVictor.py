# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:04:43 2019

@author: Gina & Hollwanncito & Crsitian
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.io import wavfile

def zerocross(l):
    newlist = l[l != 0]
    return len([x for (x, y) in zip(newlist[:-1], newlist[1:]) if x * y < 0.0])
fs, x = wavfile.read('victor.wav')

x = x.reshape(len(x), 1).astype(float) / np.max(x)

WL = 256 #Ancho de la ventana
WD = 8  # Desplazamiento de la ventana
L = x.shape[0]  #Numero de muestras de la señal de voz
NW = int((L-WL) / WD)   #Numero de ventanas
E = np.zeros(NW)        #Vector de energia por ventana
Z = np.zeros(NW)        #Vector de cruces por cero por ventana

for i in range(NW):
    a = i * WD
    y = x[ a : WL + a]
    E[i] =np.dot( y.T , y) / WL
    Z[i] = zerocross(y)
    

t = np.arange(len(x)) / fs
t1 = np.max(t) / NW * np.arange((NW)) 

#Energia normalizada
E =   10 * np.log10(E)  
E = (E - np.min(E)) / (np.max(E) - np.min(E))

#Cruce por cero normalizada
Z = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))

#GrAfIcAzIomIeNtO!!
plt.plot(t1, E)
plt.plot(t1, Z)

#t = np.arange(len(x)) / fs
plt.plot(t, x)
plt.show()
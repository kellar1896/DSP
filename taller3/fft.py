# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:18:22 2019

@author: Gina
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft


def zerocross(l):
    newlist = l[l != 0]
    return len([x for (x, y) in zip(newlist[:-1], newlist[1:]) if x * y < 0.0])
fs, x = wavfile.read('vozfemenina.wav')
x = x.reshape(len(x),).astype(float) / np.max(x)


for j in range(8,257):
    WL = j #Ancho de la ventana
    WD = 8  # Desplazamiento de la ventana
    L = x.shape[0]  #Numero de muestras de la señal de voz
    NW = int((L-WL) / WD)   #Numero de ventanas
     
    xf = np.linspace(0.0, (1/2.0*fs), WL//2)
    m = np.zeros(NW)
    for i in range(NW): 
        a = i * WD
        y = x[ a : WL + a]
        yf = fft(y)
        m[i] = xf[np.argmax(np.abs(yf[0:WL//2]))]
        
        
    #Espectro de todo el audio
    
    plt.plot(m)
    plt.show()
    print('Ventana '+str(j))

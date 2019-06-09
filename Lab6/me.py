# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:30:09 2019

@author: Gina
"""
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

def repetidor(l, r):
    c = np.zeros(len(l) * r)
    for i in range(0, len(c), len(l)):
        b = (i-len(c))*0.005
        d= -b/(1+np.abs(b))
        
        b2 = (i)*0.01
        d2= b2/(1+np.abs(b2))
        if d < 0 or d2 < 0:
            c[i:i+len(l)] = 0
        else:
            c[i:i+len(l)] = l*d*d2
        
    return c
        
fs, e = wavfile.read('e.wav')
e = e[50:83]
fs, m = wavfile.read('m.wav')

e = repetidor(e, 30)
e = e/e.max()
m = m/m.max()
me = []
cruce = 0.7
j=0
for i in range(len(e)+len(m)-int(len(m)*(1-cruce))):
    if i < len(m)*cruce:
        me.append(m[i])
    elif i < len(m):
        me.append((m[i]+e[j])*0.6)
        j += 1
    else:
        me.append(e[j])
        j += 1
        
sd.play(me, fs)

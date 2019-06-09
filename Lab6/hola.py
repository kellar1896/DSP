# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:30:09 2019

@author: Gina
"""
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

f0 = []

def repetidor(l,s):
    c = np.zeros(s*1000)
    for i in range(s*1000):
        c[i] = l[i% len(l)]
    return c
        
fs, a = wavfile.read('a.wav')
fs, hol = wavfile.read('hol.wav')
fs, o = wavfile.read('o.wav')
o_real = o[1334:3193]
a_real = o[4052:6304] 
l_real = hol[647:672]
#extension
rep_a = repetidor(a_real,1)
ol = repetidor(o_real,1)
l = repetidor(l_real,1)
#vibración
acum = 0
for n in range(len(l)):
    l[n-1] = (l[n-1]-n//2) //2
#concatenacion
olhol = np.append(ol,hol)
olholl = np.append(olhol,l)
hola = np.append(olholl,rep_a) 

sd.play(hola, fs)



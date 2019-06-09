# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:30:09 2019

@author: Gina
"""
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

def repetidor(l,s):
    c = np.zeros(s*8000)
    for i in range(s*8000):
        c[i] = l[i% len(l)]
    return c
        
fs, a = wavfile.read('a.wav')
fs, e = wavfile.read('e.wav')
fs, s = wavfile.read('s.wav')
fs, m = wavfile.read('m.wav')
fs, l = wavfile.read('l.wav')
fs, o = wavfile.read('o.wav')

me = np.append(m,e)
ol = np.append(o,l)
hola = np.append(ol,a)
am = np.append(a,m)
ama = np.append(am,a)
amas = np.append(ama,s)
holame = np.append(hola,me)
holameamas = np.append(holame,amas)
sd.play(holameamas, fs)


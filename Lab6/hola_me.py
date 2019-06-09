# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:09:11 2019

@author: Gina
"""
import sounddevice as sd
from scipy.io import wavfile
import numpy as np

f0 = []

def repetir(l,s):
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
rep_a = repetir(a_real,1)
ol = repetir(o_real,1)
l = repetir(l_real,1)
#vibración
acum = 0
for n in range(len(l)):
    l[n-1] = (l[n-1]-n//2) //2
#concatenacion
olhol = np.append(ol,hol)
olholl = np.append(olhol,l)
hola = np.append(olholl,rep_a) 



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
        
hola_me = np.append(hola,me)
sd.play(hola_me, fs)
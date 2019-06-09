# -*- coding: utf-8 -*-
import sounddevice as sd
from scipy.io import wavfile
import numpy as np


def repetidor(l,s):
    c = np.zeros(s*1000)
    for i in range(s*1000):
        c[i] = l[i% len(l)]
    return c
        
fs, a = wavfile.read('a.wav')
fs, s = wavfile.read('s.wav')
fs, m = wavfile.read('m.wav')
fs, o = wavfile.read('o.wav')

a_real = o[4052:6304] 

#repeticion

rep_a = repetidor(a_real,1)
rep_m = repetidor(m,1)



#concatenacion
am = np.append(rep_a,m)
amm = np.append(am,m)
amma = np.append(amm,rep_a) 
ammas = np.append(amma,s) 
ammass = np.append(ammas,s) 

#por si se va a la b

jijiam = np.append(rep_a,rep_m)
jijiamm = np.append(jijiam,rep_m)
jijiamma = np.append(jijiamm,rep_a) 
jijiammas = np.append(jijiamma,s) 
jijiammass = np.append(jijiammas,s) 

sd.play(ammas, fs)

sd.play(jijiammas,fs)



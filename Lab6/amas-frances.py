from matplotlib import pyplot as plt

import sounddevice as sd
from scipy.io import wavfile # as wavf
import numpy as np



def repetidor(l,s):
    c = np.zeros(s*1000)
    for i in range(s*1000):
        c[i] = l[i% len(l)]
    return c
        
fs, a = wavfile.read('a.wav')
fs, m = wavfile.read('m.wav')
fs, s1 = wavfile.read('s1.wav')

a1=s1[35700:37000]
am=s1[40000:42000]
m=s1[43700:44000]
as1=s1[44000:66000]
s=s1[70000:77000]

#concatenacion
#todo se fue a la B
aam = np.append(a1,am)

amass=np.append(aam,as1)
amas=np.append(amass,s)


#sd.play(hola, fs)


wavf.write('ama.wav', 90000,amas)

plt.plot(s1)
plt.show()




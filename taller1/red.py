# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:14:41 2019

@author: Gina
"""


import numpy as np
from tensorflow import keras
from numpy import genfromtxt

data = genfromtxt('parte1.csv', delimiter=",")
np.random.shuffle(data)
parte2 = genfromtxt('vocales.csv', delimiter=",")[:, 1]

data2 = np.zeros(int(len(parte2) / 8.0))
for i in range (len(data2)):
    data2[i] = parte2[i*8]
    
def build_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(20, activation='relu', input_shape=(2,)))
    model.add(keras.layers.Dense(3, activation='softmax'))


    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model

modelo = build_model()  # compila modelo
modelo.summary()     # resumen del modelo'''
# modelo.load_weights('modelo-2019-02-03-16.04.26.h5')


# The patience is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss',
                                           patience=5)
        
history = modelo.fit(data[:,2:4], data[:,1], epochs=1000, 
                      verbose=1, batch_size = 512, validation_split=0.3, callbacks=[early_stop])

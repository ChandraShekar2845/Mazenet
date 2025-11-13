import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# model --> y = 2x + 1
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
 
# input data & output data
x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0], dtype=float)
y = np.array([-1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
 
# define model
model = keras.Sequential([
    keras.layers.Input(shape=(1,)),
    keras.layers.Dense(units=1)
])
 
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=500, verbose=0)
 
# predict
test_input = np.array([10.0])
print(model.predict(test_input))
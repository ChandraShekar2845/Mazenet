import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd  

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)
import matplotlib.pyplot as plt
 
# pixels 0-255 -> 0-1
x_test = x_test / 255
x_train = x_train / 255
 
# step3: build nn
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), # 784
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
 
model.compile(
    optimizer="adam",
    loss='sparse_categorical_crossentropy', # integer labels
    metrics=['accuracy']
)
 
model.fit(x_train, y_train, epochs=5)
 
# performance
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
 
predictions = model.predict(x_test)
 
# display first image
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted: {np.argmax(predictions[0])}, Actual: {y_test[0]}")
plt.show()
 
import tensorflow as tf
print(tf.__version__)

import keras
print(keras.__version__)

from keras.datasets import mnist

# load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# dimensions of the tensor train_images, stored in .ndim attribute
print("train_images.ndim = ", train_images.ndim)

# shape of the tensor train_images
print("train_images.shape = ", train_images.shape)

# data type of the tensor 
print("train_images.dtype = ", train_images.dtype)

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# compile the neural network
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# preprocess the data by reshaping it into the shape that the network expects
train_images = train_images.reshape((60000, 28 * 28))

# scale the data so that all values are in the [0, 1] interval
train_images = train_images.astype('float32') / 255

# preprocess test data
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(train_images.shape)

from keras.utils import to_categorical

# categorically encode the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print(train_labels)

# train the network
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# evaluate the network
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_loss:', test_loss)
print('test_acc:', test_acc)

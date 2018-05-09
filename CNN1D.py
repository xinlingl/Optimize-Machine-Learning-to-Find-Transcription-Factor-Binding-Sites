#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:32:02 2018

@author: yangzhenyu
"""
import matplotlib
matplotlib.use('Agg')
import time
import sys  

from keras.models import Sequential  
from keras.layers import Dense, Dropout, Activation  
from keras.layers import Embedding  
from keras.layers import Conv1D, GlobalMaxPooling1D,MaxPooling1D

import one_hot_encoding_CNN as ohe 
import numpy as np  
from keras.optimizers import SGD
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
# set parameters:
epochs = int(sys.argv[4])

max_features = 15 
maxlenth = 60 
batch_size = 32  
emb_dims = 50  
filters = 25
kernel_size = 3  
hid_dimension = 250  

print('Start the program...')
time_start=time.time()

# Get input in the command line
x_train=ohe.get_list2(sys.argv[1]) 
x_val=ohe.get_list2(sys.argv[2])
x_te = ohe.get_list2(sys.argv[3])
# Get file name in the command line
y_train = np.array([ 0 for i in range(len(x_train))])
y_val = np.array([ 0 for i in range(len(x_val))])
y_te =  np.array([ 0 for i in range(len(x_te))])

# Get the y labels of the training data, test data, validation data
ind = 0
for i in range(len(y_train)):
    if ind < 19000:
        if i % 2 == 0:
            y_train[i] = 1
            ind = ind + 1
        else:
            y_train[i] = 0
            ind = ind + 1            
    else:
        y_train[i] = 0

ind = 0
for i in range(len(y_te)):
    if ind < 2056:
        if i % 2 == 0:
            y_te[i] = 1
            ind = ind + 1
        else:
            y_te[i] = 0
            ind = ind + 1            
    else:
        y_te[i] = 0

ind = 0
for i in range(len(y_val)):
    if ind < 1000:
        if i % 2 == 0:
            y_val[i] = 1
            ind = ind + 1
        else:
            y_val[i] = 0
            ind = ind + 1            
    else:
        y_val[i] = 0
      
inds = np.array([i for i in range(len(x_train))]) 
np.random.shuffle(inds) 
#print(inds) 
x_train = x_train[inds]  
y_train = y_train[inds]
  
print('Loading data...')   
#print(len(x_train), 'train sequences')  
print('The first line of the training sample is',x_train[0])  
 
print('the dimension of the training data set is', len(x_train), '*',len(x_train[0]))
print('the dimension of the validation set', len(x_val), '*',len(x_val[0]))  
  
model = Sequential()
# Add a base embedding layer
model.add(Embedding(max_features,  
                    emb_dims,  
                    input_length=maxlenth))  
model.add(Dropout(0.5))  
  
# 3 1D comvolutional layers is added, in addition a max pooling layer.  
model.add(Conv1D(filters,  
                 kernel_size,  
                 padding='valid',  
                 activation='relu',  
                 strides=1)) 
model.add(Conv1D(filters,
                 kernel_size, 
                 activation='relu'))
model.add(MaxPooling1D(3)) 
model.add(Conv1D(filters,  
                 kernel_size,  
                 padding='valid',  
                 activation='relu',  
                 strides=1))
model.add(Conv1D(filters,  
                 kernel_size,  
                 padding='valid',  
                 activation='relu',  
                 strides=1))
# Global Max Pooling layer is added  
model.add(GlobalMaxPooling1D())   
model.add(Dense(hid_dimension))  
model.add(Dropout(0.5))  
model.add(Activation('relu'))  
  
# Project the data into a sigmoid function, also act as a activation function 
model.add(Dense(1))  
model.add(Activation('sigmoid'))  
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
print('compling the model')  
model.compile(loss='binary_crossentropy',  
              optimizer=sgd,  
              metrics=['accuracy'])  
model.fit(x_train, y_train,  
          batch_size=batch_size,  
          epochs=epochs,  
          validation_data=(x_val, y_val))

classes = model.predict_classes(x_te)
test_error = 0
for i in range(len(classes)):
    if classes[i] != y_te[i]:
        test_error = test_error + 1
acc = 1 - float(test_error)/float(len(classes))
print('The test accuracy is', max(acc, 1 - acc))

time_end=time.time()
print('time cost',(time_end - time_start),'s')

fpr_keras, tpr_keras, thresholds_keras = roc_curve(classes,y_te)
plt.plot(fpr_keras, tpr_keras)
plt.savefig('CNNPerfROC.png')

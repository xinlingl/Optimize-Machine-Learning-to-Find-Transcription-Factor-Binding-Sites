
"""
Created on Mon Apr 30 18:05:18 2018

@author: yangzhenyu and xinling
"""
import matplotlib
matplotlib.use('Agg')
import sys
import one_hot_encoding_CNN as ohe
import numpy as np
from keras.preprocessing import sequence 
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers import LSTM, Activation, Dropout, TimeDistributed, Dense
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

def RNN_model(file1,file2,file3,epoch):
        x_train=ohe.get_list2(file1) 
        x_val=ohe.get_list2(file2)
        x_test = ohe.get_list2(file3)
        print("length of x_test "+str(len(x_test)))
        y_train = np.array([ 0 for i in range(len(x_train))])
        y_test = np.array([ 0 for i in range(len(x_test))])
        y_val = np.array([ 0 for i in range(len(x_val))])
        
        # Get the y labels of the training data, test data, and validation data
        ind = 0
        for i in range(len(y_train)):
            if ind < 20000:
                if i % 2 == 0:
                    y_train[i] = 1
                    ind = ind + 1
                else:
                    y_train[i] = 0
                    ind = ind + 1            
            else:
                y_train[i] = 0
        
        ind = 0
        for i in range(len(y_test)):
            if ind < 2056:
                if i % 2 == 0:
                    y_test[i] = 1
                    ind = ind + 1
                else:
                    y_test[i] = 0
                    ind = ind + 1            
            else:
                y_test[i] = 0
        
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
                
        indices = np.arange(x_train.shape[0])  
        np.random.shuffle(indices)  
        x_train = x_train[indices]  
        y_train = y_train[indices]
        maxlen = 60  
        x_train = sequence.pad_sequences(x_train, maxlen=maxlen)  
        x_test = sequence.pad_sequences(x_test, maxlen=maxlen)  
        max_features=4
        model = Sequential()
        
        #dimension of dense embedding is 256
        model.add(Embedding(max_features, output_dim=256))
        
        #long short term memroy layer is added
        model.add(LSTM(128))
        model.add(Dropout(0.5))
        
        #a dense layer is added and the activation function is sigmoid
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

        model.fit(x_train, y_train, batch_size=16, epochs=epoch, validation_data = (x_val, y_val))
        score = model.evaluate(x_test, y_test, batch_size=16)
        classes = model.predict_classes(x_test)
        test_error = 0
        
        for i in range(len(classes)):
            if classes[i] != y_test[i]:
                test_error = test_error + 1
        acc = 1 - float(test_error)/float(len(classes))
        print('The accuracy for the test set is: ', acc)
        fpr_keras, tpr_keras, thresholds_keras = roc_curve(classes,y_test)
        plt.plot(fpr_keras, tpr_keras)
        plt.savefig('RNNPerfROC.png')
        
if __name__ == "__main__":
    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    epoch = int(sys.argv[4])
    RNN_model(file1,file2,file3,epoch)


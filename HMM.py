import numpy as np
from hmmlearn import hmm
import time
import one_hot_encoding_CNN as ohe 
import sys
def get_fitted_gausshmm(X, n_components):
    """ Fit a Gaussian Hidden Markov Model to the data X.n_iter=100.
	Returns the fitted model.
    """
    # Fill in this code
    model = hmm.GaussianHMM(n_components = n_components ,n_iter=500
                            ,algorithm='viterbi')
    model.fit(X)
    return model

def get_fitted_Multinomialhmm(X, n_components):
    """ Fit a Multinomial Hidden Markov Model to the data X. n_iter=100.
	Returns the fitted model.
    """
    # Fill in this code
    model = hmm.MultinomialHMM(n_components = n_components ,n_iter=100,
                                
                               algorithm='viterbi')
    model.fit(X)
    return model

def get_y(X):
    y = []
    for i in range(len(X)):
        if i % 2 == 0:
            y.append(1)
        elif i % 2 == 1:
            y.append(0)
    return y

def get_errorate(y1,y2):
    errors = 0
    for i in range(len(y1)):
        if y1[i]!=y2[i]:
            errors = errors + 1
    a = float(errors/len(y1))
    if a > 0.5:
        return float(1 - a)
    else:
        return a


if __name__=="__main__":
    time_start=time.time()
    
    X_tr = ohe.get_list2(sys.argv[1])
    y_tr = get_y(X_tr)
    X_te = ohe.get_list2(sys.argv[2])
    y_te = get_y(X_te)
    model1 = get_fitted_gausshmm(X_tr,2)
    predicted_states1_tr= model1.predict(X_tr)
    predicted_states1_te= model1.predict(X_te)
    #print(predicted_states1)
    print('predicting with gaussian hmm...')
    print('The train error rate for gaussian hmm is ',get_errorate(y_tr,predicted_states1_tr))
    print('The test error rate for gaussian hmm is ',get_errorate(y_te,predicted_states1_te))
    
    '''
    print('predicting with multinomial hmm...')
    
    model2 = get_fitted_Multinomialhmm(X_tr,2)
    print('Building model finished!')
    predicted_states2= model2.predict(X_tr)
    print('The test error for GMM hmm is ',get_errorate(y_te,predicted_states2))
    '''
    time_end=time.time()

    print('time cost',(time_end - time_start),'s')
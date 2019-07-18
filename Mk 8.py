#Tutorial-copy

#*************************EPISODE 1*************************


import numpy as np
import os

def loadDataset():
    def download(filename, source="http://yann.lecun.com/exdb/mnist/"):
        print("Downloading ", filename)
        import urllib.request
        urllib.request.urlretrieve(source+filename, filename)

    import gzip

    def loadMnistImages(filename):
        if not os.path.exists(filename):
            download(filename)
        
        with gzip.open(filename, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
        
            data = data.reshape(-1, 1, 28, 28)

            return data/np.float32(256)

    def loadMnistLabels(filename):
        if not os.path.exists(filename):
            download(filename)

        with gzip.open(filename, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=8)

        return data

    xTrain = loadMnistImages('train-images-idx3-ubyte.gz')
    yTrain = loadMnistLabels('train-labels-idx1-ubyte.gz')
    xTest = loadMnistImages('t10k-images-idx3-ubyte.gz')
    yTest = loadMnistLabels('t10k-labels-idx1-ubyte.gz')

    return xTrain, yTrain, xTest, yTest

xTrain, yTrain, xTest, yTest = loadDataset()

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
#plt.show(plt.imshow(xTrain[1][0]))


#*************************EPISODE 2*************************


import theano
import theano.tensor as T
import lasagne

def buildNN(inputVar=None):
    lIn = lasagne.layers.InputLayer(shape=(None, 1, 28, 28), input_var = inputVar)

    lInDrop = lasagne.layers.DropoutLayer(lIn, p=0.2)

    lHid1 = lasagne.layers.DenseLayer(lInDrop, num_units = 800, nonlinearity =                                        lasagne.nonlinearities.rectify,                                                 W=lasagne.init.GlorotUniform())
    lHid1Drop = lasagne.layers.DropoutLayer(lHid1, p=.5)

    lHid2 = lasagne.layers.DenseLayer(lInDrop, num_units = 800, nonlinearity =                                        lasagne.nonlinearities.rectify,                                                 W=lasagne.init.GlorotUniform())
    lHid2Drop = lasagne.layers.DropoutLayer(lHid1, p=.5)

    lOut = lasagne.layers.DenseLayer(lHid2Drop, num_units = 10, nonlinearity =                                       lasagne.nonlinearities.softmax())

    return lOut


inputVar = T.tensor4('inputs')
targetVar = T.ivector('targets')

network = buildNN(inputVar)

prediction = lasagne.layers.get_output(network)
loss = lasagne.objectives.categorical_crossentropy(prediction, targetVar)

loss = loss.mean()

params = lasagne.layers.get_all_params(network, trainable = True)
updates = lasagne.updates.nesterov_momentum(loss, params, learning_rate = 0.01, momentum = 0.9)

trainFn = theano.function([inputVar, targetVar], loss, updates=updates)


numTrainingSteps = 250

for step in range(numTrainingSteps):
    trainErr = trainFn(xTrain, yTrain)
    print("Current step is " + str(step))


#*************************EPISODE 3*************************



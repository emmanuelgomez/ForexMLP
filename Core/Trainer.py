from keras.models import Sequential
from keras.layers import Dense
import numpy

# SGD : Método de descenso por el gradiente
# MSE : Error cuadrático medio

class Trainer:
    def __init__(self, topology, epochs = 1, lossFunction = 'mse', optimizerMethod = 'sgd', verbose = 0):
        self.topology = topology
        self.epochs = epochs
        self.lossFunction = lossFunction
        self.optimizerMethod = optimizerMethod
        self.trained = False
        self.verbose = verbose


    def LoadData(self, nValidation):
        dataLoader = DataLoader(nValidation)
        #inputLayer es un entero que contiene la cantidad de cuartetos de una misma tasa de monedas que conformaran un patron de entrada
        self.trainingData, self.validationData = dataLoader.GetTrainingData(self.topology.inputLayer);

    def SaveResults(self):
        if not self.trained:
            raise RuntimeError('The model needs to be compiled before being used.')

        sum = [0, 0, 0, 0]

        for x in range(10):
            for y in range(4):
                sum[y] += resultsList[x][y]

        mean = [0, 0, 0, 0]

        for y in range(4):
            mean[y] = sum[y] / 3

        #INSERT INTO Table Results (mean)

    def StartTrainig(self):
        ### Fix random seed ### Puede ser cualquier valor. Es importante poner un valor fijo porque se quieren comparar resultados,
        # obtenemos pesos iniciales iguales para todas las pruebas.
        numpy.random.seed(10)

        for iterator in range(1, 10):
            ### Load and prepare the dataset ###
            self.LoadData(iterator)

            ### Split into input (X) and output (Y) variables ###
            Xt = self.trainingData[:, 0: 4 * self.topology.inputLayer]
            Yt = self.trainingData[:, 4 * self.topology.inputLayer]

            Xv = self.validationData[:, 0: 4 * self.topology.inputLayer]
            Yv = self.validationData[:, 4 * self.topology.inputLayer]

            ### Create model (define the network) ###
            model = Sequential()

            # We initialize the network weights to a small random number between 0 and 0.05 because that is the default uniform weight initialization in Keras.
            # Bias Weight initialize default to 0
            # Fully connected layer and the most common type of layer used on multi-layer perceptron models.

            for x in range(0,self.topology.layers):
                if(x == 0):  # Define the input layer #
                    model.add(Dense(self.topology.neuronsPerLayers[x], input_dim=4 * self.topology.inputLayer, activation=self.topology.activationFunctionPerLayers[x]))
                else:        # Define the hidden layers and the output layer #
                    model.add(Dense(self.topology.neuronsPerLayers[x], activation=self.topology.activationFunctionPerLayers[x]))


            # Compile model (Compiling the model uses the efficient numerical libraries under the covers [TensorFloew or Theano]  to
            # chooses the best way to represent the network for training and making predictions
            model.compile(loss=self.lossFunction, optimizer=self.optimizerMethod, metrics=['accuracy'])


            # Fit the model (Train the model with our loaded data in a fix number of epochs)
            trainLoss, trainAccuracy = model.fit(Xt, Yt, epochs=self.epochs, batch_size=1, verbose=0)

            ######Puntualizar bien con Enmanuel como van a estar organizados los datos

            ### Evaluate the model ###
            valLoss, valAccuracy = model.evaluate(Xv, Yv, verbose=0)
            self.resultsList[iterator]=(trainLoss, trainAccuracy, valLoss, valAccuracy)

            if(verbose == 1):
                print("\nIteration: %.0f Loss: %.2f, Accuracy: %.2f%%" % (iterator, loss, accuracy * 100))

        self.trained = True
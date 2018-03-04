from keras.models import Sequential
from keras.layers import Dense
import numpy

class Trainer:
    def __init__(self, topology, epochs, lossFunction, optimizerMethod):
        self.topology = topology
        self.epochs = epochs
        self.lossFunction = lossFunction
        self.optimizerMethod = optimizerMethod

    def LoadData(self, nValidation):
        dataLoader = DataLoader(nValidation)
        #inputLayer es un entero que contiene la cantidad de cuartetos de una misma tasa de monedas que conformaran un patron de entrada
        self.trainingData, self.validationData = dataLoader.GetTrainingData(self.topology.inputLayer);

    def StartTrainig(self):
        ### Fix random seed ### Puede ser cualquier valor. Es importante poner un valor fijo porque se quieren comparar resultados, obtenemos pesos iniciales iguales para todas las pruebas.
        numpy.random.seed(10)

        for iterator in range(1, 10)
            ### Load and prepare the dataset ###
            self.LoadData(iterator)

            ### Split into input (X) and output (Y) variables ###
            Xt = self.trainingData[:, 0:input_dim = 4 * self.topology.inputLayer]
            Yt = self.trainingData[:, input_dim = 4 * self.topology.inputLayer]

            Xv = self.validationData[:, 0:input_dim = 4 * self.topology.inputLayer]
            Yv = self.validationData[:, input_dim = 4 * self.topology.inputLayer]

            ### Create model (define the network) ###
            model = Sequential()

            for x in range(0,self.topology.layers):
                if(x == 0)  # Define the input layer #
                    model.add(Dense(self.topology.neuronsPerLayers[x], input_dim=4 * self.topology.inputLayer, activation=self.topology.activationFunctionPerLayers[x]))
                else        # Define the hidden layers and the output layer #
                    model.add(Dense(self.topology.neuronsPerLayers[x], activation=self.topology.activationFunctionPerLayers[x]))

            #We initialize the network weights to a small random number between 0 and 0.05 because that is the default uniform weight initialization in Keras.

            # Compile model (Compiling the model uses the efficient numerical libraries under the covers [TensorFloew or Theano]  to
            # chooses the best way to represent the network for training and making predictions
            model.compile(loss=self.lossFunction, optimizer=self.optimizerMethod, metrics=['accuracy'])


            # Fit the model (Train the model with our loaded data in a fix number of epochs)
            trainLoss, trainAccuracy = model.fit(Xt, Yt, epochs=self.epochs, batch_size=1, verbose=0)

            ######Puntualizar bien con Enmanuel como van a estar organizados los datos

            ### Evaluate the model ###
            valLoss, valAccuracy = model.evaluate(Xv, Yv, verbose=0)
            self.resultsList[iterator]=(trainLoss, trainAccuracy, valLoss, valAccuracy)

            print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy * 100))
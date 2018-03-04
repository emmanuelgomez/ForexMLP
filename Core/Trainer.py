from keras.models import Sequential
from keras.layers import Dense
import numpy

class Trainer:
    def __init__(self,topology, epochs, lossFunction, optimizerMethod):
        self.topology = topology
        self.epochs = epochs
        self.lossFunction = lossFunction
        self.optimizerMethod = optimizerMethod

    def LoadData(self, nValidation):
        dataLoader = DataLoader(nValidation)
        self.trainingData, self.validationData = dataLoader.GetTrainingData(self.topology.inputLayer);

    def StartTrainig(self):
        # fix random seed for reproducibility
        numpy.random.seed(7)
        # load pima indians dataset
        dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
        # split into input (X) and output (Y) variables
        X = dataset[:, 0:8]
        Y = dataset[:, 8]
        # create model
        model = Sequential()
        for x in range(0,self.topology.layers):
            model.add(Dense(self.topology.neuronsPerLayaers[x],
                            input_dim=8, activation=self.topology.activationFunctionPerLayers[x]))

        # Compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        model.fit(X, Y, epochs=150, batch_size=10)
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

class Topology:
    def __init__(self,inputLayer,layers,neuronsPerLayaers,activationFunctionPerLayers,):
        self.inputLayer=inputLayer #Int neurons in the input layer
        self.layers=layers #Int total of layers
        self.neuronsPerLayaers=neuronsPerLayaers #Array Int neurons per layer
        self.activationFunctionPerLayers=activationFunctionPerLayers

class Topology:
    def __init__(self, id, inputLayer, layers, neuronsPerLayers, activationFunctionPerLayers):
        self.id = id
        self.inputLayer = inputLayer
        self.layers = layers
        self.neuronsPerLayers = neuronsPerLayers
        self.activationFunctionPerLayers = activationFunctionPerLayers

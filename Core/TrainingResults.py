class TrainingResults:
    def __init__(self, inputDim, weight, accuracyTraining,
                 accuracyValidation, lossTraining, lossValidation, totalEphocs, lossFunction, optimizerMethod):
        self.inputDim = inputDim
        self.weight = weight
        self.accuracyTraining = accuracyTraining
        self.accuracyValidation = accuracyValidation
        self.lossTraining = lossTraining
        self.lossValidation = lossValidation
        self.totalEphocs = totalEphocs
        self.lossFunction = lossFunction
        self.optimizerMethod = optimizerMethod
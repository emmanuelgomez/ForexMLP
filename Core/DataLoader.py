from Core.Model import Model
import random

class DataLoader:
    def __init__(self,n_Cross_Validation):
        self.n_Cross_Validation=n_Cross_Validation
        self.allDataList = []

    def GetTrainingData(self,inputDim,dataPercent):
        if len(self.allDataList)==0:
            m = Model()
            pares = m.GetAllPar()
            totalData = m.GetTotalData()
            partTotalDAta = totalData - int(totalData*(1-dataPercent))
            allData = []
            for p in pares:
                allData= allData + m.GetDataLimited(inputDim,p[0],partTotalDAta)
            self.allDataList = allData
        random.shuffle(self.allDataList)
        traingData = self.allDataList[0:int(len(self.allDataList)*0.7)]
        validationData = self.allDataList[(int(len(self.allDataList)*0.7))+1:len(self.allDataList)]
        return traingData,validationData


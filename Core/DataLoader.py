from Core.Model import Model
import random

class DataLoader:
    def __init__(self,n_Cross_Validation):
        self.n_Cross_Validation=n_Cross_Validation
        self.allDataList = []

    def GetTrainingData(self,inputDim):
        if len(self.allDataList)==0:
            m = Model()
            pares = m.GetAllPar()
            allData = []
            for p in pares:
                allData= allData + m.GetDataLimited(inputDim,p[0])
                print(p[0]+"   "+str(len(allData)))
            self.allDataList = allData
        print("len(self.allDataList)   "+str(len(self.allDataList)))
        random.shuffle(self.allDataList)
        traingData = self.allDataList[0:int(len(self.allDataList)*0.7)]
        print("int(len(self.allDataList)*0.7)" + str(int(len(self.allDataList)*0.7)))
        print("len(self.traingData)   " + str(len(traingData)))
        print("len(self.allDataList)   " + str(len(self.allDataList)))
        print("(int(len(self.allDataList)*0.7))+1   " + str((int(len(self.allDataList)*0.7))+1))
        validationData = self.allDataList[(int(len(self.allDataList)*0.7))+1:len(self.allDataList)]
        print("len(self.validationData)   " + str(len(validationData)))
        print(traingData[126])
        print(traingData[126][0])
        print(traingData[126][1])
        print(validationData[589])
        print(validationData[589][0])
        print(validationData[589][1])
        return traingData,validationData


# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject


import HandleData


class Control:

    linePointer = 0


    def __init__(self):



        pass

    def startControl(self):
        print("Coming")
        handleData = HandleData.HandleData()

        extractedData, self.linePointer, loopFlag = handleData.extractData(self.linePointer)
        if loopFlag == False:
            return

        extractedDataList = extractedData.split('\n')

        print("extractedData: ", extractedData)



        i = 0
        for i in range(len(extractedDataList)):
            print(extractedDataList[i])
            info = handleData.analyzeLineInfo(extractedDataList[i])

            print("list :  ", extractedDataList[i])

            print("TYPE:   ", type(info))


        #self.setQmlProperty()



    def setQmlProperty(self, window):

        qObject = window.findChild(QObject, "dateText")
        qObject.setProperty("text", self.linePointer)


    def printDebug(self):
        print("wait")











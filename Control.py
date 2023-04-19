# This Python file uses the following encoding: utf-8
import HandleData


class Control:


    extractedData = ""
    lineCount = 0

    def __init__(self):
        pass

    def startControl(self):
        handleData = HandleData.HandleData()

        extractedData, lineCount = handleData.extractData()
        extractedDataList = extractedData.split('\n')


        for i in range(lineCount):
            GGAInfo = handleData.analyzeLineInfo(extractedDataList[i])

            self.debugPrint(GGAInfo)










        return


    def debugPrint(self, GGAInfo):
        print("Time: ", GGAInfo.time)

        print("Lat: ", GGAInfo.latDirection, GGAInfo.coordY)
        print("Lon: ", GGAInfo.latDirection, GGAInfo.coordX)

        print("Alt: ", GGAInfo.altitude)
        print("")






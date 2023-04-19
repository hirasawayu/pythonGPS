# This Python file uses the following encoding: utf-8
import HandleData


class Control:

    def __init__(self):
        pass

    def startControl(self):
        handleData = HandleData.HandleData()

        linePointer = 0
        while True:
            extractedData, linePointer, loopFlag = handleData.extractData(linePointer)
            if loopFlag == False:
                break
            extractedDataList = extractedData.split('\n')

            print("THRO")



            i = 0
            print("NUM        ",  len(extractedDataList))
            for i in range(len(extractedDataList)):
                print(extractedDataList[i])
                GGAInfo = handleData.analyzeLineInfo(extractedDataList[i])


                if not GGAInfo == 0:
                    self.debugPrint(GGAInfo)

        return


    def debugPrint(self, GGAInfo):
        print("Time: ", GGAInfo.time)

        print("Lat: ", GGAInfo.latDirection, GGAInfo.coordY)
        print("Lon: ", GGAInfo.latDirection, GGAInfo.coordX)

        print("Alt: ", GGAInfo.altitude)
        print("")






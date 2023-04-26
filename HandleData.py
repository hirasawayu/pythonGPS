# This Python file uses the following encoding: utf-8

import Data

class HandleData:

    direction = 0
    directionValidFlag = False

    def __init__(self):

        pass

    def extractData(self, linePointer):

        file = open('NMEA.txt', 'r')
        extractedData = ""

        for i in range(linePointer):
            file.readline()

        while True:

            line = file.readline()

            if line == ("\n"):
                linePointer += 1
                loopFlag = True
                break

            elif not line:
                loopFlag = False
                break

            linePointer += 1

            extractedData += line

            if "#GPVTG" in line:
                loopFlag = True
                break

        file.close()

        return extractedData, linePointer, loopFlag


    def analyzeLineInfo(self, line):

        result = self.checkSum(line)

        if result == False:
            print("CheckSum Does Not Match or Space")
            return 0

        #チェックサム部分を切り取り
        line = line[:-3]

        if "$GPGGA" in line:
            componentList = line.split(',')

        #componentList
        #[1]:time
        #[2]:latitude
        #[3]:latDirection
        #[4]:longtitude
        #[5]:lonDirection
        #[6]:locationQuality
        #[7]:usingSatelliteNum
        #[9]:altitude
        #[11]:geoidHeight



            GGAInfo = Data.GGAData(componentList)
            #GGAInfo.debugPrint()

            return GGAInfo

        elif "$GPRMC" in line:
            componentList = line.split(',')

            #componentList
            #[7]:speed
            #[8]:direction
            #[9]:date

            RMCInfo = Data.RMCData(componentList)
            #RMCInfo.debugPrint()

            if (componentList[2] == "A"):
                self.direction = float(componentList[8])
                self.directionValidFlag = True


            return RMCInfo

        elif "$GPGSV" in line:
            componentList = line.split(',')

            #componentList
            #[1]:totalSentenceNum
            #[2]:sentenceNo
            #[3]:totalSatelliteNum
            #[4 + 4n]:satelliteNo
            #[5 + 4n]:satelliteElevationAngle
            #[6 + 4n]:satelliteDirection
            #[7 + 4n]:satelliteCNoise

            if self.directionValidFlag == False:
                return 0


            GSVInfo = Data.GSVData(componentList, self.direction)
            #GSVInfo.debugPrintAll()

            return GSVInfo

        else:

            return 0






    def checkSum(self, line):

        self.count = 0
        sum = line[-2:]

        checkLine = line[1:-3]
        checkLine = bytes(checkLine, encoding= "utf-8")

        for i in range(len(checkLine)):
            self.count ^= checkLine[i]

        self.count = ("%X" % self.count)

        if self.count == sum:
            return True

        else:
            return False






















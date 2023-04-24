# This Python file uses the following encoding: utf-8


class Data:

    """
    #GGA
    time = ""
    latitude = ""
    longtitude = 0
    #使用衛星数
    usingSatelliteNum = 0
    #海抜
    altitude = 0
    #ジオイド高
    geoidHeight = 0
    #X座標
    coordX = 0
    #Y座標
    coordY = 0
    #位置特定品質
    locationQuality = 0

    #RMC
    speed = 0
    direction = 0
    date = ""
    """


    def __init__(self):
        pass

    def debugPrint(self):
        pass

class GGAData (Data):

    objectNameList = ["timeText", "latText", "lonText", "satelliteNumText", "altText", "geoidHeightText", "coordXText", "coordYText", "locationQualityText", "circleColorText"]
    loop = 10
    locationQualitySentence = ["Undefined", "SPS", "Differential GPS"]
    circleColorSentence = ["black", "blue", "green"]

    def __init__ (self, componentList, lat_degree, lon_degree, coordX, coordY):

        self.time = componentList[1][:2] + ":" + componentList[1][2:4] + ":" + componentList[1][4:]
        self.latitude = "Lat: " + componentList[3] + "  " + str(lat_degree)
        self.longtitude = "Lon: " + componentList[5] + "  " + str(lon_degree)
        self.usingSatelliteNum = "Number of Using Satellites: " + componentList[7]
        self.altitude = "Alt: " + componentList[9] + " m"
        self.geoidHeight = "Geoid Height: " + componentList[11] + " m"
        self.coordX = "Coord X: " + str(coordX)
        self.coordY = "Coord Y: " + str(coordY)
        self.locationQuality = "LocationQuality: " + self.locationQualitySentence[int(componentList[6])]
        self.circleColor = self.circleColorSentence[int(componentList[6])]

        self.infoList = [self.time, self.latitude, self.longtitude, self.usingSatelliteNum, self.altitude, self.geoidHeight, self.coordX, self.coordY, self.locationQuality, self.circleColor]

        pass

    def debugPrint(self):
        print(self.time)
        print(self.latitude)
        print(self.longtitude)
        print(self.usingSatelliteNum)
        print(self.altitude)
        print(self.geoidHeight)
        print(self.coordX)
        print(self.coordY)
        print("")


class RMCData(Data):

    objectNameList = ["speedText", "directionText", "dateText"]
    loop = 3

    def __init__ (self, componentList):

        self.speed = "Spd: " + str(float(componentList[7]) * 1.852) + " km/h"
        self.direction = "Direction: " + componentList[8] + " degree"
        self.date = "(UTC) " + "20" + componentList[9][4:] + "/" + componentList[9][2:4] + "/" + componentList[9][:2]

        self.infoList = [self.speed, self.direction, self.date]

        pass

    def debugPrint(self):
        print(self.speed)
        print(self.direction)
        print(self.date)
        print("")


class GSVData(Data):

    #objectNameList: ["satelliteNo(n)", "satelliteElevationAngle(n)", "satelliteDirection(n)", satelliteExplanation(n)]
    loop = 4
    infoList = []
    objectNameList = []


    def __init__ (self, componentList):

        self.totalSatelliteNum = componentList[3]
        self.countGSV = ((int(componentList[2]) - 1) * 4)

        for i in range(4):

            self.countGSV += 1
            arrayPosition = (((self.countGSV - 1) % 4) * 4)

            self.satelliteNo = componentList[4 + arrayPosition]
            self.satelliteElevationAngle = componentList[5 + arrayPosition]
            self.satelliteDirection = componentList[6 + arrayPosition]
            self.satelliteExplanation = "#" + '%04d' % int(componentList[4 + arrayPosition]) + ":" + componentList[7 + arrayPosition] + "dB"

            self.satelliteNoName = "satelliteNoText" + str(self.countGSV)
            self.satelliteElevationAngleName = "satelliteElevationAngleText" + str(self.countGSV)
            self.satelliteDirectionName = "satelliteDirectionText" + str(self.countGSV)
            self.satelliteExplanationName = "satelliteExplanationText" + str(self.countGSV)

            self.infoList += [self.satelliteNo, self.satelliteElevationAngle, self.satelliteDirection, self.satelliteExplanation]
            self.objectNameList += [self.satelliteNoName, self.satelliteElevationAngleName, self.satelliteDirectionName, self.satelliteExplanationName]

            self.debugPrintPartial()

            if self.countGSV == componentList[3]:
                self.loop = i + 1
                break

        pass

    def debugPrintPartial(self):
        print("totalSatelliteNum: ", self.totalSatelliteNum)
        print("countGSV: ", self.countGSV)
        print(self.satelliteNoName, " : ", self.satelliteNo)
        print(self.satelliteElevationAngleName, " : ", self.satelliteElevationAngle)
        print(self.satelliteDirectionName, " : ", self.satelliteDirection)
        print(self.satelliteExplanationName, " : ", self.satelliteExplanation)


    def debugPrintAll(self):

        print("ALL PRINT")
        for i in range (self.loop * 4):
            print(self.infoList[i], " : ", self.objectNameList[i])







# This Python file uses the following encoding: utf-8
from pyproj import Transformer
import math

class Data:

    #GGA
    time = "--:--:--"
    latitude = "Lat: ---"
    longtitude = "Lon: ---"
    #使用衛星数
    usingSatelliteNum = "Number of Using Satellites: ---"
    #海抜
    altitude = "Alt: ---"
    #ジオイド高
    geoidHeight = "Geiod Height: ---"
    #X座標
    coordX = "Coord X: ---"
    #Y座標
    coordY = "Coord Y: ---"
    #位置特定品質
    locationQuality = "LocationQuality: ---"

    #RMC
    speed = "Spd: ---"
    direction = "Direction: ---"
    date = "--/--/--"
    northDirection = 0

    #GSV
    satelliteNum = ""
    satelliteCoordX = 180
    satelliteCoordY = 180
    satelliteViewColor = "grey"
    satelliteVisible = "false"
    satelliteExplanation = ""

    def __init__(self):
        pass

    def debugPrint(self):
        pass


class GGAData (Data):

    objectNameList = ["timeText", "locationQualityText", "satelliteNumText", "circleColorText", "latText", "lonText", "altText", "geoidHeightText", "coordXText", "coordYText"]
    propertyList = ["text", "text", "text", "text", "text", "text", "text", "text", "text", "text"]
    locationQualitySentence = ["Undefined", "SPS", "Differential GPS"]
    circleColorSentence = ["black", "blue", "green"]

    def __init__ (self, componentList):

        self.time = componentList[1][:2] + ":" + componentList[1][2:4] + ":" + componentList[1][4:]
        self.locationQuality = "LocationQuality: " + self.locationQualitySentence[int(componentList[6])]
        self.usingSatelliteNum = "Number of Using Satellites: " + componentList[7]
        self.circleColor = self.circleColorSentence[int(componentList[6])]

        if componentList[6] == "1" or componentList[6] == "2":

            lat_degree, lon_degree = self.degminToDegree(componentList[2], componentList[4])
            coordX, coordY = self.latlonToXY(lat_degree, componentList[3], lon_degree, componentList[5])

            latCenter, lonCenter = self.findCenter(componentList[2], componentList[4])
            self.latitude = "Lat: " + componentList[3] + "  " + componentList[2][:-7] + "." + componentList[2][-7:-5] + "'" + componentList[2][-4:-2] + "." + componentList[2][-2:] + "\""
            self.longtitude = "Lon: " + componentList[5] + "  " + componentList[4][:-7] + "." + componentList[4][-7:-5] + "'" + componentList[4][-4:-2] + "." + componentList[4][-2:] + "\""
            self.altitude = "Alt: " + componentList[9] + " m"
            self.geoidHeight = "Geoid Height: " + componentList[11] + " m"
            self.coordX = "Coord X: " + str(coordX)
            self.coordY = "Coord Y: " + str(coordY)

        #無効データの場合
        """
        else:
            self.latitude = "Lat: ---"
            self.longtitude = "Lon: ---"
            self.altitude = "Alt : ---"
            self.geoidHeight = "Geiod Height: ---"
            self.coordX = "Coord X: ---"
            self.coordY = "Coord Y: ---"

        """

        self.infoList = [self.time, self.locationQuality, self.usingSatelliteNum, self.circleColor, self.latitude, self.longtitude, self.altitude, self.geoidHeight, self.coordX, self.coordY]
        self.loop = len(self.infoList)

        return

    #緯度経度の小数点の位置を求める
    def findCenter(self, latitude, longtitude):
        latCenter = latitude.find(".")
        lonCenter = longtitude.find(".")

        return latCenter, lonCenter


    #緯度経度の単位を度分から度に変換
    def degminToDegree(self, latitude, longtitude):
        #緯度
        lat_degmin = float(latitude)
        lat_int = int(lat_degmin/100)
        lat_float = ( lat_degmin - (lat_int * 100) ) /60
        lat_degree = lat_int + lat_float

        #経度
        lon_degmin = float(longtitude)
        lon_int = int(lat_degmin/100)
        lon_float = ( lon_degmin - (lat_int * 100) ) /60
        lon_degree = lon_int + lon_float

        return lat_degree, lon_degree


    #緯度経度からXY座標を求める
    def latlonToXY(self, lat_degree, latDirection, lon_degree, lonDirection):

        transformer = Transformer.from_crs("EPSG:6668", "EPSG:6680")
        y_tmp, x_tmp = transformer.transform(lat_degree, lon_degree)

        #North:+, South:-
        if latDirection == 'N':
            y = y_tmp

        elif latDirection == 'S':
            y = -(y_tmp)

        else:
            print("NO DATA")


        #East:+, West:-
        if lonDirection == 'E':
            x = x_tmp

        elif lonDirection == 'W':
            x = -(x_tmp)

        else:
            print("NO DATA")

        return x, y

    def debugPrint(self):
        for i in range(self.loop):
            print("GGA[" , i , "]: ", self.infoList[i])

        print("")


class RMCData(Data):

    objectNameList = ["dateText", "speedText", "directionText", "northPointerRotation",]
    propertyList = ["text", "text", "text", "angle"]

    def __init__ (self, componentList):

        self.date = "(UTC) " + "20" + componentList[9][4:] + "/" + componentList[9][2:4] + "/" + componentList[9][:2]

        #無効なデータの場合
        if componentList[2] == "A":

            self.speed = "Spd: " + '{:.2f}'.format(float(componentList[7]) * 1.852) + " km/h"
            if componentList[8] != "":
                self.direction = "Direction: " + componentList[8] + " degree"
                self.northDirection = float(componentList[8]) - 180

            self.infoList = [self.date, self.speed, self.direction, self.northDirection]


        else:
            #self.speed = "Spd: --- km/h"
            #self.direction = "Direction: --- degree"

            self.infoList = [self.date, self.speed, self.direction]

        self.loop = len(self.infoList)


        return

    def debugPrint(self):

        for i in range(self.loop):
            print("RMC[" , i , "]: ", self.infoList[i])

        print("")


class GSVData(Data):

    infoList =[]
    objectNameList = []
    propertyList = []

    def __init__ (self, componentList, direction):

        self.totalSatelliteNum = int(componentList[3])
        self.countGSV = ((int(componentList[2]) - 1) * 4)

        #初期化データをセット
        if componentList[2] == "1":
            self.clearCache()

        for i in range(4):

            self.countGSV += 1

            if self.countGSV <= self.totalSatelliteNum:

                arrayPosition = (((self.countGSV - 1) % 4) * 4)
                self.satelliteElevationAngle = int(componentList[5 + arrayPosition])
                self.satelliteDirection = int(componentList[6 + arrayPosition]) - float(direction)


                self.satelliteNo = componentList[4 + arrayPosition]
                self.satelliteCoordX, self.satelliteCoordY = self.calculation(direction)
                if componentList[7 + arrayPosition] != "":
                    self.satelliteViewColor = self.setSatelliteViewColor(int(componentList[7 + arrayPosition]))
                self.satelliteVisible = "true"
                self.satelliteExplanation = "#" + '%04d' % int(componentList[4 + arrayPosition]) + ":" + componentList[7 + arrayPosition] + "dB"

            #データが無い場合は初期化
            else:
                self.satelliteNum = ""
                self.satelliteCoordX = 180
                self.satelliteCoordY = 180
                self.satelliteViewColor = "grey"
                self.satelliteVisible = "false"
                self.satelliteExplanation = ""

            self.satelliteNoName = "satelliteViewText" + str(self.countGSV)
            self.satelliteViewName = "satelliteView" + str(self.countGSV)
            self.satelliteViewTextName = "satelliteExplanationText" + str(self.countGSV)

            self.infoList += [self.satelliteNo, self.satelliteCoordX, self.satelliteCoordY, self.satelliteViewColor, self.satelliteVisible, self.satelliteExplanation]
            self.objectNameList += [self.satelliteNoName, self.satelliteViewName, self.satelliteViewName, self.satelliteViewName, self.satelliteViewName, self.satelliteViewTextName]
            self.propertyList += ["text", "x", "y", "color", "visible", "text"]

            #self.debugPrintPartial()

        self.loop = len(self.infoList)

        pass

    def clearCache(self):

        for i in range(1, 15):
            self.infoList += ["false", ""]
            self.objectNameList += ["satelliteView" + str(i), "satelliteExplanationText" + str(i)]
            self.propertyList += ["visible", "text"]


    def calculation(self, directionNum):

        length = self.satelliteElevationAngle / 90 * 200

        satelliteCoordX = 180 + (math.sin(math.radians(self.satelliteDirection - directionNum))) * length
        satelliteCoordY = 180 + (math.cos(math.radians(self.satelliteDirection - directionNum))) * length

        return satelliteCoordX, satelliteCoordY

    def setSatelliteViewColor(self, CNoise):

        if CNoise >= 40:
            return "brown"

        elif (CNoise >= 20) & (CNoise < 40):
            return "black"

        else:
            return "grey"




    def debugPrintPartial(self):

        print("totalSatelliteNum: ", self.totalSatelliteNum)
        print("countGSV: ", self.countGSV)
        print(self.satelliteNoName, " : ", self.satelliteNo)
        print(self.satelliteViewName)
        print("coordX: ", self.satelliteCoordX)
        print("coordY: ", self.satelliteCoordY)
        print(self.satelliteViewTextName, " : ", self.satelliteExplanation)
        print("satelliteDirection: ", self.satelliteDirection)
        print("")


    def debugPrintAll(self):

        print("ALL PRINT")
        for i in range (self.loop):
            print(self.infoList[i], " : ", self.objectNameList[i])

        print("")







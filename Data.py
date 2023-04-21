# This Python file uses the following encoding: utf-8


class Data:

    #GGA
    time = ""
    latitude = ""
    #0 = North; 1 = South
    latDirection = 0
    longtitude = 0
    #0 = East; 1 = West
    lonDirection = 0
    #位置特定品質
    locationQuality = 0
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

    #RMC
    speed = 0
    direction = 0
    date = ""



    def __init__(self):
        pass

    def debugPrint(self):
        pass

class GGAData (Data):

    def __init__ (self, time, latitude, latDirection, longtitude, lonDirection, locationQuality, usingSatelliteNum, altitude, geoidHeight, coordX, coordY):
        self.time = time
        self.latitude = latitude
        self.latDirection = latDirection
        self.longtitude = longtitude
        self.lonDirection = lonDirection
        self.locationQuality = locationQuality
        self.usingSatelliteNum = usingSatelliteNum
        self.altitude = altitude
        self.geoidHeight = geoidHeight
        self.coordX = coordX
        self.coordY = coordY

        pass

    def debugPrint(self):
        print("Time: ", self.time)

        print("Lat: ", self.latDirection, self.coordY)
        print("Lon: ", self.latDirection, self.coordX)

        print("Alt: ", self.altitude)
        print("")


class RMCData(Data):

    def __init__ (self, speed, direction, date):
        self.speed = speed
        self.direction = direction
        self.date = date

        pass

    def debugPrint(self):
        print("Speed: ", self.speed)
        print("Direction: ", self.direction)
        print("Date: ", self.date)
        print("TimeO:  ", self.time)
        print("")




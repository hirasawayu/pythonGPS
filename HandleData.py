# This Python file uses the following encoding: utf-8
from pyproj import Transformer
from time import sleep
import Data

class HandleData:

    def __init__(self):

        pass

    def extractData(self, linePointer):

        file = open('NMEA.txt', 'r')
        extractedData = ""
        lineCount = 0


        for i in range(linePointer):
            file.readline()

        while True:
            line = file.readline()

            if line == "\n":
                linePointer += 1
                loopFlag = True
                break

            elif not line:
                loopFlag = False

            linePointer += 1

            extractedData += line

        file.close()

        return extractedData, linePointer, loopFlag


    def analyzeLineInfo(self, line):


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
        #[10]:geoidHeight

            time = componentList[1][:2] + ":" + componentList[1][2:4] + ":" + componentList[1][4:]

            lat_degree, lon_degree = self.degminToDegree(componentList[2], componentList[4])

            coordX, coordY = self.latlonToXY(lat_degree, componentList[3], lon_degree, componentList[5])

            #self.checkSum()

            #Timer
            sleep(1)

            GGAInfo = Data.Data(time, componentList[2], componentList[3], componentList[4], componentList[5], componentList[6], componentList[7], componentList[9], componentList[11], coordX, coordY)

        else:
            GGAInfo = 0

        return GGAInfo



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



    def checkSum(self):

       str = "GPGGA,234248,3926.5029,N,11946.1984,W,2,12,0.8,1381.7,M,-22.0,M,,"
       sum = 0
       pointer = 0


       #for i in range(len(str)):
        #   byte = str[pointer].encode
         #  byte = bytearray(byte)
          # print(byte)
           #pointer += 1




















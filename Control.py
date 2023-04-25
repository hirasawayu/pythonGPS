# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject
from PySide6.QtCore import QTimer

import HandleData

class Control:

    linePointer = 0


    def __init__(self, window):

        #windowオブジェクトのポインタを取得
        self.window = window

        #タイマーセット
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.startControl)
        self.timer.start()

        pass

    def startControl(self):

        handleData = HandleData.HandleData()
        extractedData, self.linePointer, loopFlag = handleData.extractData(self.linePointer)
        if loopFlag == False:

            self.timer.stop()
            return

        extractedDataList = extractedData.split('\n')

        i = 0
        for i in range(len(extractedDataList)):
            print(extractedDataList[i])
            info = handleData.analyzeLineInfo(extractedDataList[i])

            if info != 0:
                self.setInfo(info)


    def setQmlProperty(self, objectName, propertyName, info):

        qObject = self.window.findChild(QObject, objectName)
        qObject.setProperty(propertyName, info)


    def setInfo(self, info):

        for i in range(info.loop):
            self.setQmlProperty(info.objectNameList[i], info.propertyList[i], info.infoList[i])


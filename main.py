# This Python file uses the following encoding: utf-8

from pathlib import Path
import urllib.request
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import  QQuickWindow
from PySide6.QtCore import QTimer



import Control


def main():


    app = QGuiApplication()

    engine = QQmlApplicationEngine()
    engine.load("mainWindow.qml")
    if not engine.rootObjects():
        return -1

    window = QQuickWindow()
    window = engine.rootObjects()[0]
    window.show()

    control = Control.Control()

    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(control.startControl)
    timer.start()



    sys.exit(app.exec())


if __name__ == "__main__":
    main()

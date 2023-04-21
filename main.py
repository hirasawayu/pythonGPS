# This Python file uses the following encoding: utf-8

from pathlib import Path
import urllib.request
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import  QQuickWindow



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

    control = Control.Control(window)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

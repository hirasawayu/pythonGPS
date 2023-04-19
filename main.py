# This Python file uses the following encoding: utf-8

from pathlib import Path
import urllib.request
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView, QQuickWindow
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject

import Control


def main():


    app = QApplication()

    engine = QQmlApplicationEngine()
    engine.load("mainWindow.qml")
    if not engine.rootObjects():
        return -1

    window = QQuickWindow()
    window = engine.rootObjects()[0]
    window.show()
    qObject = engine.rootObjects()[0].findChild(QObject, "text1")
    qObject.setProperty("text", "Changed")

    #インスタンス生成
    control = Control.Control()
    control.startControl()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

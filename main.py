# This Python file uses the following encoding: utf-8

from pathlib import Path
import urllib.request
import sys
import toml.encoder

from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, QUrl

import Control


def main():


    app = QApplication()
    view = QQuickView()
    view.setSource("mainWindow.qml")
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()

    engine = QQmlApplicationEngine()
    engine.load("mainWindow.qml")

    rootObject = engine.rootObjects()

    qObject = QObject()

    #qObject = rootObject.find("text1")
    qObject.setProperty("text", "Changed")

    #インスタンス生成
    control = Control.Control()
    #control.startControl()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

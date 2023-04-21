import QtQuick 2.15
import QtQuick.Window 2.15

Window {
//Rectangle {
    id: window
    width: 900
    height: 600
    visible: true

    Text {
        id: dateText
        objectName: "dateText"
        width: 300
        height: 30
        text: "(UTC) --/--/--"
        anchors.left: parent.left
        anchors.top: parent.top
        font.pixelSize: 25
        anchors.topMargin: 10
        anchors.leftMargin: 480
    }

    Text {
        id: timeText
        objectName: "timeText"
        width: 300
        height: 40
        text: qsTr("--:--:--")
        anchors.left: dateText.left
        anchors.top: dateText.bottom
        font.pixelSize: 30
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.topMargin: 5
        anchors.leftMargin: 0
    }

    Text {
        id: latText
        objectName: "latText"
        width: 400
        height: 40
        text: qsTr("Lat: ---")
        anchors.left: timeText.left
        anchors.top: timeText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        font.family: "Arial"
        anchors.leftMargin: 0
        anchors.topMargin: 10
    }

    Text {
        id: lonText
        objectName: "lonText"
        width: 400
        height: 40
        text: qsTr("Lon: ---")
        anchors.left: latText.left
        anchors.top: latText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        font.family: "Arial"
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Text {
        id: speedText
        objectName: "speedText"
        width: 400
        height: 40
        text: qsTr("Spd: ---")
        anchors.left: latText.left
        anchors.top: lonText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        font.family: "Arial"
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Text {
        id: altText
        objectName:  "altText"
        width: 400
        height: 40
        text: qsTr("Alt : ---")
        anchors.left: latText.left
        anchors.top: speedText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        font.family: "Arial"
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Text {
        id: drcText
        objectName:  "drcText"
        width: 400
        height: 40
        text: qsTr("Drc: ---")
        anchors.left: latText.left
        anchors.top: altText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Rectangle {
        id: largeCircle
        width: 400
        height: 400
        color: "#ffffff"
        radius: width * 0.5
        border.width: 2
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.leftMargin: 30
        anchors.topMargin: 100

        Rectangle {
            id: smallCircle
            width: 200
            height: 200
            color: "#ffffff"
            radius: width * 0.5
            border.width: 2
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Rectangle {
            id: holiLine
            width: 400
            height: 2
            color: "#ffffff"
            border.width: 2
            anchors.verticalCenter: parent.verticalCenter
        }

        Rectangle {
            id: vertLine
            width: 2
            height: 400
            color: "#ffffff"
            border.width: 2
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}

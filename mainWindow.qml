import QtQuick 2.15
import QtQuick.Window 2.15

Window {
//Rectangle {
    id: window
    width: 900
    height: 600
    visible: true
    color: "black"

    Text {
        id: dateText
        objectName: "dateText"
        color: "white"
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
        color: "white"
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
        color: "white"
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
        color: "white"
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
        color: "white"
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
        objectName: "altText"
        color: "white"
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
        objectName:  "directionText"
        color: "white"
        width: 400
        height: 40
        text: qsTr("Direction: ---")
        anchors.left: latText.left
        anchors.top: altText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Text {
        id: geoidHeightText
        objectName:  "geoidHeightText"
        color: "white"
        width: 400
        height: 40
        text: qsTr("Geiod Height: ---")
        anchors.left: latText.left
        anchors.top: drcText.bottom
        font.pixelSize: 25
        verticalAlignment: Text.AlignVCenter
        anchors.leftMargin: 0
        anchors.topMargin: 0
    }

    Rectangle {
        id: largeCircle
        color: circleColor
        border.color: "white"
        width: 400
        height: 400
        radius: width * 0.5
        border.width: 2
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.leftMargin: 30
        anchors.topMargin: 100

        property alias circleColor: circleColorText.text


        Rectangle {
            id: smallCircle
            color: circleColor
            border.color: "white"
            width: 200
            height: 200
            radius: width * 0.5
            border.width: 2
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            property alias circleColor: circleColorText.text
        }


        Rectangle {
            id: holiLine
            color: "white"
            border.color: "white"
            width: 400
            height: 2
            border.width: 2
            anchors.verticalCenter: parent.verticalCenter
        }

        Rectangle {
            id: vertLine
            color: "white"
            border.color: "white"
            width: 2
            height: 400
            border.width: 2
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: coordXText
            objectName: "coordXText"
            color: "white"
            width: 300
            height: 30
            text: qsTr("Coord X: ---")
            anchors.top: parent.bottom
            font.pixelSize: 20
            verticalAlignment: Text.AlignVCenter
            anchors.topMargin: 10
        }

        Text {
            id: coordYText
            objectName: "coordYText"
            color: "white"
            width: 300
            height: 30
            text: qsTr("Coord Y: ---")
            anchors.left: parent.left
            anchors.top: coordXText.bottom
            font.pixelSize: 20
            verticalAlignment: Text.AlignVCenter
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: circleColorText
            objectName: "circleColorText"
            visible: false
            text: "black"
            font.pixelSize: 12


        }
    }

    Text {
        id: locationQualityText
        objectName: "locationQualityText"
        color: "white"
        width: 300
        height: 30
        text: qsTr("Location Quality: ---")
        anchors.left: parent.left
        anchors.top: parent.top
        font.pixelSize: 20
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        anchors.leftMargin: 10
        anchors.topMargin: 5
    }

    Text {
        id: satelliteNumText
        objectName: "satelliteNumText"
        color: "white"
        width: 300
        height: 30
        text: qsTr("Number of Using Satellites: ---")
        anchors.left: parent.left
        anchors.top: locationQualityText.bottom
        font.pixelSize: 20
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        anchors.topMargin: 0
        anchors.leftMargin: 10
    }

    Rectangle {
        id: showGSVArea
        width: 400
        height: 220
        color: "black"
        anchors.left: dateText.left
        anchors.top: parent.top
        anchors.leftMargin: 0
        anchors.topMargin: 360

        Text {
            id: satelliteExplanationText1
            objectName: "satelliteExplanationText1"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.top: parent.top
            font.pixelSize: 22
            color: "white"
            verticalAlignment: Text.AlignVCenter
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText2
            objectName: "satelliteExplanationText2"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText1.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText3
            objectName: "satelliteExplanationText3"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText2.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText4
            objectName: "satelliteExplanationText4"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText3.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText5
            objectName: "satelliteExplanationText5"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText4.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText6
            objectName: "satelliteExplanationText6"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText5.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText7
            objectName: "satelliteExplanationText7"
            height: 30
            text: qsTr("")
            anchors.left: parent.left
            anchors.right: satelliteExplanationText1.right
            anchors.top: satelliteExplanationText6.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText8
            objectName: "satelliteExplanationText8"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText1.right
            anchors.top: parent.top
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 50
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText9
            objectName: "satelliteExplanationText9"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText8.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText10
            objectName: "satelliteExplanationText10"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText9.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText11
            objectName: "satelliteExplanationText11"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText10.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText12
            objectName: "satelliteExplanationText12"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText11.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText13
            objectName: "satelliteExplanationText13"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText12.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }

        Text {
            id: satelliteExplanationText14
            objectName: "satelliteExplanationText14"
            width: 150
            height: 30
            text: qsTr("")
            anchors.left: satelliteExplanationText8.left
            anchors.top: satelliteExplanationText13.bottom
            font.pixelSize: 22
            verticalAlignment: Text.AlignVCenter
            color: "white"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }
    }

}

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "PixelBar" as PB

ApplicationWindow {
    id: window
    visible: true
    visibility: "FullScreen"
    width: 1920
    height: 1080

    background: Rectangle {
        color: "black"
    }


    Row {
        spacing: 20

        PB.Button {
            text: "Test"
            onClicked: checked = !checked
            autoResetInterval: 2000
        }

        PB.Label {
            text: (app != null) ? app.test : ""
        }

        PB.Slider {
            id: slider
            orientation: Qt.Horizontal
        }

        PB.Label {
            id: value
            text: slider.value.toFixed(2)
            onTextChanged: function(text) {
                graph.addValue(parseFloat(text))
            }
        }

        PB.SparkLine {
            id: graph
        }

        Item {
            width: childrenRect.width
            height: parent.height
            PB.Label {
                text: graph.max.toFixed(2)
                color: "green"
                font.pointSize: 20
                anchors.top: parent.top
            }
            PB.Label {
                text: graph.min.toFixed(2)
                color: "green"
                font.pointSize: 20
                anchors.bottom: parent.bottom
            }
        }
    }
}

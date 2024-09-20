// Copyright (C) 2024 twyleg
import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

import "./items"

ApplicationWindow {
	id: window

    width: 800
	height: 480
	visible: true
	title: qsTr("Stopwatch")

	color: "black"


	Item {
		id: dialItem

        height: parent.height
        width: height

        anchors.left: parent.left
        anchors.top: parent.top

		Dial {
			id: dial

			anchors.centerIn: parent
			diameter: Math.min(parent.width, parent.height)
		}
	}


    ListView {
        id: timerList

        height: parent.height

        anchors.top: parent.top
        anchors.left: dialItem.right
        anchors.right: parent.right

        model: stopwatch_model.timers

        delegate: Text {
            id: lightFunctionDelegate

            width: parent.width
            height: 40

            color: "white"

            text: model.modelData.name + "\n" + model.modelData.hours + ":" + model.modelData.seconds + ":" + model.modelData.millis

            MouseArea {
                anchors.fill: parent
                onClicked: stopwatch_model.activate_timer(model.modelData)
            }

        }


    }


}

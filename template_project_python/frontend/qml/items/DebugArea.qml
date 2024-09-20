// Copyright (C) 2022 twyleg
import QtQuick 2.0

MouseArea {
	id: debugArea

	property alias borderColor: rectangle.border.color

	anchors.fill: parent
	onClicked: printDebug(mouse)

	function printDebug(mouse) {
		var relX = mouse.x/debugArea.width;
		var relY = mouse.y/debugArea.height;
		console.log("Click coordinates [px] (x/y): (" + mouse.x + "/" + mouse.y + ")");
		console.log("Click coordinates [%]  (x/y): (" + relX + "/" + relY + ")");
	}

	Rectangle {
		id: rectangle

		anchors.fill: parent
		color: "transparent"
		border.width: 1
		border.color: "white"
	}
}

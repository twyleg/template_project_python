// Copyright (C) 2022 twyleg
import QtQuick 2.0

Item {
	id: dial

	property int diameter

	property color fontColor: "#FF929292"

	width: diameter
	height: diameter

	enum State {
		RESET = 0,
		RUNNING = 1,
		PAUSED = 2
	}

	FontLoader {
		id: fontLoader
		source: "../../fonts/karnivore_krate.ttf"
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_background.svg"
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_milliseconds.svg"
        rotation: 360 * (stopwatch_model.active_timer.millis / 1000.0)
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_seconds.svg"
        rotation: 360 * (stopwatch_model.active_timer.seconds / 60)
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_minutes.svg"
        rotation: 360 * (stopwatch_model.active_timer.minutes / 60)
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_hours.svg"
        rotation: 360 * (stopwatch_model.active_timer.hours / 24)
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_start_stop_button_inactive.svg"
		visible: !startStopButtonMouseArea.containsPress
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_start_stop_button_active.svg"
		visible: startStopButtonMouseArea.containsPress
	}

	Text {
		id: startStopButtonText
        text: stopwatch_model.active_timer.state !== Dial.State.RUNNING ? "start" : "stop"

		anchors.centerIn: parent
		anchors.verticalCenterOffset: -parent.width * 0.17

		color: parent.fontColor
		font.family: fontLoader.name
		font.pixelSize: parent.height * 0.03
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_reset_button_inactive.svg"
        visible: stopwatch_model.active_timer.state === Dial.State.PAUSED && !resetButtonMouseArea.containsPress
	}

	Svg {
		anchors.fill: parent

		source: "../../images/svg_extracted_layers/stopwatch_reset_button_active.svg"
        visible: stopwatch_model.active_timer.state === Dial.State.PAUSED && resetButtonMouseArea.containsPress
	}

    MouseArea {

        anchors.fill: parent

        onPressed: stopwatch_model.add_timer()
    }

	MouseArea {
		id: startStopButtonMouseArea

		anchors.centerIn: parent
		anchors.verticalCenterOffset: -parent.width * 0.16

		width: parent.width * 0.38
		height: parent.height * 0.11

        onPressed: {
            console.info("Start/Stop button clicked!")
            stopwatch_model.active_timer.start_stop()
        }
	}

	MouseArea {
		id: resetButtonMouseArea

        enabled: stopwatch_model.active_timer.state === Dial.State.PAUSED

		anchors.centerIn: parent
		anchors.verticalCenterOffset: -parent.width * 0.12

		width: parent.width * 0.13
		height: parent.height * 0.05

        onPressed: {
            console.info("Reset button clicked!")
            stopwatch_model.active_timer.reset()
        }
	}

    Timer {
        id: pauseAnimationTimer

		interval: 500
		repeat: true
        running: stopwatch_model.active_timer.state === Dial.State.PAUSED
		triggeredOnStart: true

		onTriggered: {
			if(Qt.colorEqual(dial.fontColor, "#FF929292")) {
				dial.fontColor = "red"
			} else {
				dial.fontColor = "#FF929292"
			}
		}

		onRunningChanged: {
			if (running === false){
				dial.fontColor = "#FF929292"
			}
		}
	}

	Text {
		id: timeDescText
		text: "hh     mm     ss"

		anchors.horizontalCenter: parent.horizontalCenter
		anchors.bottom: timeText.top

		color: parent.fontColor
		font.family: fontLoader.name
		font.pixelSize: parent.height * 0.025
	}

	Text {
		id: timeText
        text: String(stopwatch_model.active_timer.hours).padStart(2, '0') + ":" + String(stopwatch_model.active_timer.minutes).padStart(2, '0') + ":" + String(stopwatch_model.active_timer.seconds).padStart(2, '0')

		anchors.centerIn: parent

		color: parent.fontColor
		font.family: fontLoader.name
		font.pixelSize: parent.height * 0.09
	}

	Text {
		id: millisDescText
		text: "ms"

		anchors.horizontalCenter: parent.horizontalCenter
		anchors.top: timeText.bottom

		color: parent.fontColor
		font.family: fontLoader.name
		font.pixelSize: parent.height * 0.025
	}

	Text {
		id: millisText
        text: String(stopwatch_model.active_timer.millis).padStart(3, '0')

		anchors.horizontalCenter: parent.horizontalCenter
		anchors.top: millisDescText.bottom

		color: parent.fontColor
		font.family: fontLoader.name
		font.pixelSize: parent.height * 0.09
	}
}

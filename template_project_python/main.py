# Copyright (C) 2024 twyleg
import argparse
import logging
import time
from enum import IntEnum
from pathlib import Path

from simple_python_app_qt.qml_application import QmlApplication
from simple_python_app_qt.property import Property, PropertyMeta

from PySide6.QtCore import QObject, Signal, Slot, QTimer

from template_project_python import __version__


FILE_DIR = Path(__file__).parent


class State(IntEnum):
    RESET = 0
    RUNNING = 1
    PAUSED = 2


class Timer(QObject, metaclass=PropertyMeta):
    name = Property(str)
    state = Property(int)
    millis = Property(int)
    seconds = Property(int)
    minutes = Property(int)
    hours = Property(int)

    def __init__(self, name: str, millis: int = 0, seconds: int = 0, minutes: int = 0, hours: int = 0) -> None:
        QObject.__init__(self)
        self.name = name  # type: ignore
        self.state = State.RESET  # type: ignore
        self.millis = millis  # type: ignore
        self.seconds = seconds  # type: ignore
        self.minutes = minutes  # type: ignore
        self.hours = hours  # type: ignore

        self.count_ns = 0
        self.last_timestamp_ns = 0

        self.logm = logging.getLogger(name)

    @Slot()
    def start(self) -> None:
        self.last_timestamp_ns = time.time_ns()
        self.state = State.RUNNING  # type: ignore
        self.logm.info("Started")

    @Slot()
    def pause(self) -> None:
        self.state = State.PAUSED  # type: ignore
        self.logm.info("Paused at %d", self.count_ns)

    @Slot()
    def reset(self) -> None:
        self.logm.info("Reset at %d", self.count_ns)
        self.count_ns = 0
        self.state = State.RESET  # type: ignore
        self.update()

    @Slot()
    def start_stop(self) -> None:
        state = self.state
        if state == State.RESET:  # type: ignore
            self.start()
        elif state == State.PAUSED:  # type: ignore
            self.start()
        elif state == State.RUNNING:  # type: ignore
            self.pause()

    def update(self):
        if self.state == State.RUNNING:
            current_timestamp_ns = time.time_ns()
            diff = current_timestamp_ns - self.last_timestamp_ns
            self.count_ns += diff
            self.last_timestamp_ns = current_timestamp_ns

        count_ms = self.count_ns // (1000 * 1000)

        self.millis = count_ms % 1000
        self.seconds = (count_ms // 1000) % 60
        self.minutes = (count_ms // (1000 * 60)) % 60
        self.hours = count_ms // (1000 * 60 * 60)


class StopwatchModel(QObject, metaclass=PropertyMeta):

    active_timer = Property(Timer)
    timers = Property(list)

    def __init__(self) -> None:
        QObject.__init__(self)
        self.logm = logging.getLogger("stopwatch_model")
        self.timer_counter = 0
        self.timers = []  # type: ignore
        self.add_timer()
        self.active_timer = self.timers[0]  # type: ignore

    @Slot()
    def add_timer(self):
        self.timer_counter += 1
        timer_name = f"Timer {self.timer_counter}"
        self.timers.append(Timer(timer_name))
        self.logm.info("Added timer: %s", timer_name)

    @Slot(Timer)
    def activate_timer(self, timer: Timer):
        self.active_timer = timer  # type: ignore
        self.logm.info("Activated timer: %s", timer.name)

    def update_timers(self) -> None:
        for timer in self.timers:  # type: ignore
            timer.update()


class Application(QmlApplication):

    def __init__(self):
        # fmt: off
        super().__init__(
            application_name="template_project_python",
            version=__version__,
            application_config_schema_filepath=FILE_DIR / "resources/application_config_schema.json",
            logging_logfile_output_dir= Path.cwd() / "logs/",
            frontend_qml_file_path=FILE_DIR / "frontend/qml/main.qml"
        )
        # fmt: on

        self.stopwatch_model = StopwatchModel()
        self.add_model(self.stopwatch_model, "stopwatch_model")

        self.timer = QTimer()
        self.timer.timeout.connect(self.stopwatch_model.update_timers)
        self.timer.start()

    def add_arguments(self, argparser: argparse.ArgumentParser):
        pass

    def run(self, args: argparse.Namespace):
        self.open()


def main() -> None:
    application = Application()
    application.start()


if __name__ == "__main__":
    main()

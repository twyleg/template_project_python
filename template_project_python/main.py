# Copyright (C) 2024 twyleg
import sys
import argparse

from pathlib import Path
from simple_python_app.generic_application import GenericApplication

from template_project_python import __version__


FILE_DIR = Path(__file__).parent


class Application(GenericApplication):

    def __init__(self):
        super().__init__(
            application_name="template_project_python",
            version=__version__,
            application_config_schema_filepath=FILE_DIR / "resources/application_config_schema.json"
        )

    def add_arguments(self, argparser: argparse.ArgumentParser):
        self.logm.info("init_argparse()")

        argparser.add_argument("--example", type=str, default=None, help="Example")

    def run(self, args: argparse.Namespace):
        self.logm.info("run()")
        self.logm.debug("run()")

        self.logm.info("Config: %s", self.application_config)


def main() -> None:
    application = Application()
    application.start(sys.argv[1:])


if __name__ == "__main__":
    main()

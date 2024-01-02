# Copyright (C) 2023 twyleg
import sys
import argparse
import logging

from pathlib import Path
from template_project_python import __version__

FILE_DIR = Path(__file__).parent
FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


def main() -> None:
    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

    parser = argparse.ArgumentParser(usage="template_project_python <command> [<args>] <files>")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    args = parser.parse_args(sys.argv[1:2])

    logging.info("FILE_DIR: %s", FILE_DIR)
    with open(FILE_DIR / "resources/test_data.txt") as input_file:
        logging.info("The data: %s", input_file.read())


if __name__ == "__main__":
    main()

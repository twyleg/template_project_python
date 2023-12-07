# Copyright (C) 2023 twyleg
import sys
import argparse
import logging
import yaml

from pathlib import Path
from template_project_utils import __version__
from template_project_utils.initializer import init_template

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"

FILE_DIR = Path(__file__).parent


def main() -> None:

    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

    parser = argparse.ArgumentParser(usage="template_project_utils <command> [<args>] <files>")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    args = parser.parse_args(sys.argv[1:2])



if __name__ == "__main__":
    main()

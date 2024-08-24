# Copyright (C) 2023 twyleg
import os
import sys
import argparse
import logging
import logging.config
import yaml

from pathlib import Path
from template_project_python import __version__

FILE_DIR = Path(__file__).parent

LOGGING_CONFIG_NAME = "logging.yaml"
LOGGING_DEFAULT_FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


logger = logging.getLogger("main")


def init_argparser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(usage="template_project_python <command> [<args>] <files>")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    return parser.parse_args(sys.argv[1:2])


def init_logging() -> None:
    try:
        with open(LOGGING_CONFIG_NAME, 'r') as f:
            d = yaml.safe_load(f)
            logging.config.dictConfig(d)
        logger.info("Logging config loaded from file: %s", LOGGING_CONFIG_NAME)
    except FileNotFoundError:
        logging.basicConfig(stream=sys.stdout, format=LOGGING_DEFAULT_FORMAT, level=logging.INFO, force=True)
        logger.info("No logging config (%s) found. Using default settings!", LOGGING_CONFIG_NAME)
    except (ValueError, TypeError, AttributeError, ImportError) as e:
        logger.error("Error reading logging config (%s):", LOGGING_CONFIG_NAME)
        logger.error(e)
        logger.error("Exiting...")
        sys.exit(os.EX_CONFIG)


def main() -> None:
    args = init_argparser()
    init_logging()

    logger.info("FILE_DIR: %s", FILE_DIR)
    with open(FILE_DIR / "resources/test_data.txt") as input_file:
        logger.info("The data: %s", input_file.read())


if __name__ == "__main__":
    main()

# Copyright (C) 2023 twyleg
import sys
import argparse

from template_project_python import __version__


def main() -> None:
    parser = argparse.ArgumentParser(usage="inkscape_layer_utils <command> [<args>] <track_file>")
    parser.add_argument("command", help="track_generator commands")
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

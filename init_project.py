#!/usr/bin/env python3
import fileinput
import sys
from pathlib import Path

FILE_DIR = Path(__file__).parent
TEMPLATE_NAME = "template_project_python"


def replace_string_in_file(filepath: Path, text_to_search: str, replacement_text: str) -> int:
    with fileinput.FileInput(filepath, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


def rename(project_name: str) -> None:
    replace_string_in_file(FILE_DIR / "docs/index.rst", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "docs/conf.py", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "template_project_python/__main__.py", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "template_project_python/main.py", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / ".gitattributes", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "README.rst", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "MANIFEST.in", TEMPLATE_NAME, project_name)
    replace_string_in_file(FILE_DIR / "setup.py", TEMPLATE_NAME, project_name)

    Path(FILE_DIR / TEMPLATE_NAME).rename(FILE_DIR / project_name)


if __name__ == "__main__":
    project_name = sys.argv[1]
    rename(project_name)
    
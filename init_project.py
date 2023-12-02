#!/usr/bin/env python3
import fileinput
from pathlib import Path

FILE_DIR = Path(__file__).parent

def replace_string_in_file(filepath: Path, text_to_search: str, replacement_text: str) -> int:
    with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

def

def replace() -> None:

    template_name = "template_project_python"
    project_name = "foo_bar"

    replace_string_in_file(FILE_DIR / "docs/index.rst", template_name, project_name)
    replace_string_in_file(FILE_DIR / "docs/conf.py", template_name, project_name)
    replace_string_in_file(FILE_DIR / "template_project_python/__main__.py", template_name, project_name)
    replace_string_in_file(FILE_DIR / "template_project_python/main.py", template_name, project_name)
    replace_string_in_file(FILE_DIR / ".gitattributes", template_name, project_name)
    replace_string_in_file(FILE_DIR / "README.rst", template_name, project_name)
    replace_string_in_file(FILE_DIR / "setup.py", template_name, project_name)


    Path(FILE_DIR / template_name).rename(FILE_DIR / project_name)
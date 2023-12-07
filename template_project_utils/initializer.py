# Copyright (C) 2023 twyleg
import logging
import yaml
import jsonschema
import json

from pathlib import Path

FILE_DIR = Path(__file__).parent


def load_config(config_path: Path) -> dict:
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def update_files(update_files: dict) -> None:
    for file in update_files:
        for path in file:
            logging.info("Updating file: %s", path)
        for rules in file.values():
            for rule in rules:
                for old, new in rule.items():
                    logging.info("  \"%s\" -> \"%s\"", old, new)


def rename_files(rename_files: dict) -> None:
    logging.info("Renaming files:")
    for entry in rename_files:
        for old, new in entry.items():
            logging.info("  %s -> %s", old, new)


def remove_files(remove_files: dict) -> None:
    logging.info("Removing files:")
    for remove_file in remove_files:
        logging.info("  %s", remove_file)


def remove_dirs(remove_dirs: dict) -> None:
    logging.info("Removing dirs:")
    for remove_dir in remove_dirs:
        logging.info("  %s", remove_dir)


def init_template(config_path: Path):
    config = load_config(config_path)

    logging.debug("Config: %s", config)

    with open(FILE_DIR / "schemas/config.json") as config_schema_file:
        config_schema = json.load(config_schema_file)
        jsonschema.validate(instance=config, schema=config_schema)

    update_files_dict = config["update_files"]
    update_files(update_files_dict)

    rename_files_dict = config["rename_files"]
    rename_files(rename_files_dict)

    remove_files_dict = config["remove_files"]
    remove_files(remove_files_dict)

    remove_dirs_dict = config["remove_dirs"]
    remove_dirs(remove_dirs_dict)


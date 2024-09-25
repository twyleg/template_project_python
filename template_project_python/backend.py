# Copyright (C) 2024 twyleg
import json
import logging
import os

import jsonschema
from datetime import datetime, date
from typing import List, Any, Dict

from playhouse.shortcuts import model_to_dict
from playhouse.reflection import generate_models
from pathlib import Path
from peewee import Database, PostgresqlDatabase, fn, SqliteDatabase

import template_project_python.data_model as data_model


FILE_DIR = Path(__file__).parent


class BackendError(Exception):
    pass


class EntityAccess:
    def __init__(self, entity_type, json_schema_filepath: Path):
        self.entity_type = entity_type
        with open(json_schema_filepath) as json_schema_file:
            self.json_schema = json.load(json_schema_file)

    @classmethod
    def _serialize_defaults(cls, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Type not serializable: {obj}")

    @classmethod
    def _serialize(cls, dic: Dict[str, Any]) -> str:
        return json.dumps(dic, default=cls._serialize_defaults, indent=4)

    def create(self, entity_dict: Dict[str, Any]) -> str:
        jsonschema.validate(instance=entity_dict, schema=self.json_schema)
        created_entity = self.entity_type.create(**entity_dict)
        return self._serialize(model_to_dict(created_entity))

    def get_all(self) -> str:
        query = self.entity_type.select()
        entity_list = [model_to_dict(entity) for entity in query]
        return self._serialize({"entities": entity_list})

    def get(self, id: int) -> str:
        entity = self.entity_type.get_by_id(id)
        return self._serialize(model_to_dict(entity, backrefs=True))

    def update(self, id: int, entity_dict: Dict[str, Any]) -> None:
        jsonschema.validate(instance=entity_dict, schema=self.json_schema)
        self.entity_type.set_by_id(id, entity_dict)

    def delete(self, id: int) -> None:
        self.entity_type.get_by_id(id).delete_instance()


class NamedEntityAccess(EntityAccess):
    def __init__(self, entity_type, json_schema_filepath: Path):
        super().__init__(entity_type, json_schema_filepath)

    def get_by_name(self, name: str):
        entity = self.entity_type.get(self.entity_type.name == name)
        return self._serialize(model_to_dict(entity))

    def update_by_name(self, name: str, entity_dict: Dict[str, Any]) -> None:
        jsonschema.validate(instance=entity_dict, schema=self.json_schema)
        self.entity_type.update(**entity_dict).where(self.entity_type.name == name).execute()

    def delete_by_name(self, name: str) -> None:
        self.entity_type.delete().where(self.entity_type.name == name).execute()


class Backend:

    ENTITIES = [
        data_model.Shelf,
        data_model.Item
    ]

    @classmethod
    def create_database_sql_lite(cls) -> Database:
        return SqliteDatabase("warehouse.db")

    @classmethod
    def create_database_postgres(cls) -> Database:
        pg_user = os.environ["PG_USER"]
        pg_password = os.environ["PG_PASSWORD"]
        pg_host = os.environ["PG_HOST"]
        pg_port = os.environ["PG_PORT"]
        pg_dbname = os.environ["PG_DBNAME"]

        return PostgresqlDatabase(pg_dbname, user=pg_user, password=pg_password, host=pg_host, port=int(pg_port))

    def __init__(self):
        logging.info("Backend created!")

        self.database = self.create_database_sql_lite()
        self.database.bind(self.ENTITIES)
        self.database.create_tables(self.ENTITIES)

        self.shelf = EntityAccess(data_model.Shelf, FILE_DIR / "schemas/shelf.json")
        self.item = EntityAccess(data_model.Item, FILE_DIR / "schemas/item.json")

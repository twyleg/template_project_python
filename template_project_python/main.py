# Copyright (C) 2023 twyleg
from typing import Any

import sys
import argparse
import logging
import json

from pathlib import Path
from template_project_python import __version__

from flask import Flask, request, Response
from werkzeug.exceptions import HTTPException, NotFound

from template_project_python.backend import Backend
from template_project_python.crud_controller import CrudController

FILE_DIR = Path(__file__).parent
FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


app = Flask(__name__)
backend = Backend()


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


# def successful_create(response: str) -> Response:
#     return Response(response=response, status=201, mimetype="application/json")
#
#
# def successful_read(response: str) -> Response:
#     return Response(response=response, status=200, mimetype="application/json")
#
#
# def successful_update() -> Response:
#     return Response(status=204)
#
#
# def successful_delete() -> Response:
#     return Response(status=204)


# def add_crud_operations(entity: Any, name: str, create_enabled=False, read_enabled=False, update_enabled=False, delete_enabled=False):
#     def create() -> Response:
#         body = request.get_json(force=True)
#         new_object = entity.create(body)
#         return successful_create(new_object)
#
#     def read_by_id(id: int) -> Response:
#         return successful_read(entity.get(id))
#
#     def read_all() -> Response:
#         return successful_read(entity.get_all())
#
#     def update(id: int) -> Response:
#         body = request.get_json(force=True)
#         entity.update(id, body)
#         return successful_update()
#
#     def delete(id: int) -> Response:
#         entity.delete(id)
#         return successful_delete()
#
#     if create_enabled:
#         app.add_url_rule(f"/{name}", endpoint=f"create_{name}", view_func=create, methods=["POST"])
#
#     if read_enabled:
#         app.add_url_rule(f"/{name}", endpoint=f"read_{name}_all", view_func=read_all, methods=["GET"])
#         app.add_url_rule(f"/{name}/<int:id>", endpoint=f"read_{name}_by_id", view_func=read_by_id, methods=["GET"])
#
#     if update_enabled:
#         app.add_url_rule(f"/{name}/<int:id>", endpoint=f"update_{name}", view_func=update, methods=["PUT"])
#
#     if delete_enabled:
#         app.add_url_rule(f"/{name}/<int:id>", endpoint=f"delete_{name}", view_func=delete, methods=["DELETE"])



# @flask_app.route("/api/shelf/", methods=["POST"])
# def shelf_create() -> Response:
#     body = request.get_json(force=True)
#     new_object = backend.shelf.create(body)
#     return successful_create(new_object)
#
#
# @flask_app.route("/api/shelf", defaults={"id": None}, methods=["GET"])
# @flask_app.route("/api/shelf/<int:id>", methods=["GET"])
# def shelf_read(id: int | None) -> Response:
#     if id is not None:
#         return successful_read(backend.shelf.get(id))
#     else:
#         return successful_read(backend.shelf.get_all())
#
#
# @flask_app.route("/api/shelf/<int:id>", methods=["PUT"])
# def shelf_update(id: int) -> Response:
#     body = request.get_json(force=True)
#     backend.shelf.update(id, body)
#     return successful_update()
#
#
# @flask_app.route("/api/shelf/<int:id>", methods=["DELETE"])
# def shelf_delete(id: int) -> Response:
#     backend.shelf.delete(id)
#     return successful_delete()


# @flask_app.route("/api/test/<id>", methods=["GET"])
# def test_get_by_id(id: int) -> str | Response:
#     try:
#         return storage.test_get_by_id(id)
#     except Exception as e:
#         return Response(status=404)
#
#
# @flask_app.route("/api/test/<name>", methods=["GET"])
# def test_get_by_name(name: str) -> str | Response:
#     try:
#         return storage.test_get_by_name(name)
#     except Exception as e:
#         return Response(status=404)


@app.route("/")
def index():
    raise NotFound

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

    # add_crud_operations(backend.shelf, "shelf", create_enabled=True, read_enabled=True, update_enabled=True,
    #                     delete_enabled=True)
    # add_crud_operations(backend.item, "item", create_enabled=True, read_enabled=True, update_enabled=True,
    #                     delete_enabled=True)

    crud_controllers = [
        CrudController(app, backend.shelf, "shelf"),
        CrudController(app, backend.item, "item")
    ]

    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()

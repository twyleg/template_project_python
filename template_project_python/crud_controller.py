from typing import Any

import flask
from flask import Response, request


def successful_create(response: str) -> Response:
    return Response(response=response, status=201, mimetype="application/json")


def successful_read(response: str) -> Response:
    return Response(response=response, status=200, mimetype="application/json")


def successful_update() -> Response:
    return Response(status=204)


def successful_delete() -> Response:
    return Response(status=204)


class CrudController:

    def __init__(self, app: flask.app, entity: Any, name: str, route_prefix="", create_enabled=True,
                 read_enabled=True, update_enabled=True, delete_enabled=True):
        self.app = app
        self.entity = entity
        self.route_prefix = route_prefix
        self.name = name

        self.create_enabled = create_enabled
        self.read_enabled = read_enabled
        self.update_enabled = update_enabled
        self.delete_enabled = delete_enabled

        self.route = f"{route_prefix}/{name}"

        if self.create_enabled:
            self.app.add_url_rule(self.route, endpoint=f"create_{name}", view_func=self.create, methods=["POST"])

        if self.read_enabled:
            self.app.add_url_rule(self.route, endpoint=f"read_{name}_all", view_func=self.read_all, methods=["GET"])
            self.app.add_url_rule(f"{self.route}/<int:id>", endpoint=f"read_{name}_by_id", view_func=self.read_by_id,
                             methods=["GET"])

        if self.update_enabled:
            self.app.add_url_rule(f"{self.route}/<int:id>", endpoint=f"update_{name}", view_func=self.update, methods=["PUT"])

        if self.delete_enabled:
            self.app.add_url_rule(f"{self.route}/<int:id>", endpoint=f"delete_{name}", view_func=self.delete, methods=["DELETE"])

    def create(self) -> Response:
        body = request.get_json(force=True)
        new_object = self.entity.create(body)
        return successful_create(new_object)

    def read_by_id(self, id: int) -> Response:
        return successful_read(self.entity.get(id))

    def read_all(self) -> Response:
        return successful_read(self.entity.get_all())

    def update(self, id: int) -> Response:
        body = request.get_json(force=True)
        self.entity.update(id, body)
        return successful_update()

    def delete(self, id: int) -> Response:
        self.entity.delete(id)
        return successful_delete()

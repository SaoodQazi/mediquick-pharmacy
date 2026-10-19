from flask import Blueprint, request, jsonify

bp = Blueprint("users", __name__)
USERS = {}


@bp.post("/register")
def register():
    data = request.get_json(force=True)
    USERS[data["email"]] = {"name": data["name"], "password": data["password"]}
    return jsonify(message="Registration successful"), 201

import re

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

bp = Blueprint("users", __name__)
USERS = {}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@bp.post("/register")
def register():
    data = request.get_json(force=True)
    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not name or not EMAIL_RE.match(email) or len(password) < 8:
        return jsonify(error="Invalid name, email or password (min 8 chars)"), 400
    if email in USERS:
        return jsonify(error="Email already registered"), 409

    USERS[email] = {"name": name, "password_hash": generate_password_hash(password)}
    return jsonify(message="Registration successful"), 201

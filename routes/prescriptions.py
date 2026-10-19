import os

from flask import Blueprint, request, jsonify

bp = Blueprint("prescriptions", __name__)
PRESCRIPTIONS = []
ALLOWED = {".pdf", ".png", ".jpg", ".jpeg"}
MAX_BYTES = 5 * 1024 * 1024


@bp.post("/prescriptions")
def upload_prescription():
    file = request.files.get("file")
    if file is None:
        return jsonify(error="No file uploaded"), 400

    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in ALLOWED:
        return jsonify(error="Only PDF, PNG or JPG files are allowed"), 400

    content = file.read()
    if len(content) > MAX_BYTES:
        return jsonify(error="File too large (max 5 MB)"), 413

    PRESCRIPTIONS.append({"filename": file.filename, "size": len(content)})
    return jsonify(message="Prescription uploaded"), 201

from flask import Blueprint, request, jsonify

bp = Blueprint("prescriptions", __name__)
PRESCRIPTIONS = []


@bp.post("/prescriptions")
def upload_prescription():
    file = request.files.get("file")
    if file is None:
        return jsonify(error="No file uploaded"), 400
    PRESCRIPTIONS.append({"filename": file.filename})
    return jsonify(message="Prescription uploaded"), 201

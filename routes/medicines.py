from flask import Blueprint, request, jsonify

bp = Blueprint("medicines", __name__)
MEDICINES = [
    {"id": 1, "name": "Paracetamol 500mg", "price": 30, "in_stock": True},
    {"id": 2, "name": "Amoxicillin 250mg", "price": 120, "in_stock": True},
    {"id": 3, "name": "Cetirizine 10mg", "price": 45, "in_stock": False},
]


@bp.get("/medicines")
def list_medicines():
    q = request.args.get("q", "").strip().lower()
    results = [m for m in MEDICINES if q in m["name"].lower()]
    return jsonify(results)

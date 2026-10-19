from flask import Blueprint, jsonify, request

api_bp = Blueprint("api", __name__, url_prefix="/api")

# In-memory catalog of pharmacy medicines
MEDICINES = [
    {"id": 1, "name": "Paracetamol", "dosage": "500mg", "stock": 100, "price": 5.99},
    {"id": 2, "name": "Amoxicillin", "dosage": "250mg", "stock": 50, "price": 12.50},
    {"id": 3, "name": "Ibuprofen", "dosage": "400mg", "stock": 75, "price": 8.20},
    {"id": 4, "name": "Cetirizine", "dosage": "10mg", "stock": 120, "price": 6.45},
]


@api_bp.route("/medicines", methods=["GET"])
def get_medicines():
    """Retrieve list of available medicines."""
    return jsonify({"success": True, "data": MEDICINES}), 200


@api_bp.route("/medicines/<int:med_id>", methods=["GET"])
def get_medicine(med_id):
    """Retrieve details of a single medicine by ID."""
    med = next((m for m in MEDICINES if m["id"] == med_id), None)
    if not med:
        return jsonify({"success": False, "error": "Medicine not found"}), 404
    return jsonify({"success": True, "data": med}), 200


@api_bp.route("/orders", methods=["POST"])
def place_order():
    """Place a new pharmacy order."""
    data = request.get_json() or {}
    items = data.get("items", [])
    if not items:
        return jsonify({"success": False, "error": "No items specified"}), 400

    total = 0.0
    for item in items:
        med_id = item.get("medicine_id")
        qty = item.get("quantity", 1)
        med = next((m for m in MEDICINES if m["id"] == med_id), None)
        if not med:
            return jsonify({"success": False, "error": f"Medicine {med_id} not found"}), 404
        if med["stock"] < qty:
            return jsonify({"success": False, "error": f"Insufficient stock for {med['name']}"}), 400
        med["stock"] -= qty
        total += med["price"] * qty

    return jsonify({
        "success": True,
        "message": "Order placed successfully",
        "order": {
            "order_id": 1001,
            "items": items,
            "total_price": round(total, 2),
            "status": "confirmed"
        }
    }), 201

from flask import Blueprint, jsonify

bp = Blueprint("orders", __name__)
ORDERS = {1001: {"status": "Packed"}}


@bp.get("/orders/<int:order_id>/status")
def order_status(order_id):
    order = ORDERS.get(order_id)
    if order is None:
        return jsonify(error="Order not found"), 404
    return jsonify(order_id=order_id, status=order["status"])

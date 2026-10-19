from flask import Flask, jsonify
from routes import api_bp


def create_app(config=None):
    """Application factory for MediQuick Pharmacy."""
    app = Flask(__name__)

    if config:
        app.config.update(config)

    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return jsonify({
            "service": "MediQuick Pharmacy API",
            "version": "1.0.0",
            "status": "online",
            "endpoints": {
                "health": "/health",
                "medicines": "/api/medicines",
                "orders": "/api/orders"
            }
        }), 200

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

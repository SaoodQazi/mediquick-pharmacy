import importlib
import pkgutil

from flask import Flask

import routes


def create_app():
    app = Flask(__name__)
    # auto-register every blueprint found in the routes/ folder
    for module_info in pkgutil.iter_modules(routes.__path__):
        module = importlib.import_module(f"routes.{module_info.name}")
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)

    @app.get("/")
    def health():
        return {"project": "MediQuick", "status": "running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

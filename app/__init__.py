from flask import Flask


def create_app():
    app = Flask(__name__)

    # Change this to a secure key in production
    app.config["SECRET_KEY"] = "potatoes"

    # Import and register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app

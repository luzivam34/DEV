# Import from flask Library
from flask import Flask

# Creating the Create_app() function
def create_app():
    app = Flask(__name__)

    # import routes
    from app.routes.route_main import main_bp


    # register routes
    app.register_blueprint(main_bp)

    return app


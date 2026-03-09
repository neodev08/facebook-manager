from flask import Flask
from flask_cors import CORS

from routes.auth import auth_routes
from routes.pages import pages_routes
from routes.posts import posts_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth_routes)
    app.register_blueprint(pages_routes)
    app.register_blueprint(posts_routes)

    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)


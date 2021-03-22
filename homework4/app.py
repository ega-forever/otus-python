from flask import Flask
from views.landing import landing_app

app = Flask(__name__, static_folder="static")

app.register_blueprint(landing_app, prefix="/")


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=8080,
        debug=True
    )
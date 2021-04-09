from flask import Flask
from flask_migrate import Migrate, upgrade
from models.db import db
from views.landing import landing_app

app = Flask(__name__, static_folder="static")
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)

app.register_blueprint(landing_app, prefix="/")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=app.config.get('APP_PORT'),
        debug=app.config.get('APP_DEBUG')
    )
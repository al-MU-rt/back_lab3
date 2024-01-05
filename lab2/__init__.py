from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgresql_c7bt_user:HUzGHcedHqw9WygX6Z4io770rg5kuXQ5@dpg-cmbeqs8cmk4c73dg0m40-a.oregon-postgres.render.com/postgresql_c7bt"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import lab2.views
import lab2.models

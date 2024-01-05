from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost/laba3"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import lab2.views
import lab2.models
from datetime import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/sensorReadings.db'
db = SQLAlchemy(app)

# Declare Model
class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    stamp = db.Column(db.DateTime)

    def __init__(self, value, stamp=None):
        self.value = value
        if stamp is None:
            stamp = datetime.utcnow()
        self.stamp = stamp

    def __repr__(self):
        return '<Post %r>' % self.title

db.create_all()
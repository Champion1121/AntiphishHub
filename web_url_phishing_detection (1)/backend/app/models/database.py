
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2083), nullable=False)
    is_phishing = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

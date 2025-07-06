
from flask import Flask
from flask_cors import CORS
from app.models.database import db
from app.routes.url_checker import url_checker
from app.routes.admin import admin
from app.routes.export import export

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/phishing_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app)

app.register_blueprint(url_checker)
app.register_blueprint(admin)
app.register_blueprint(export)

@app.route('/')
def home():
    return 'Phishing Detection API is running.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

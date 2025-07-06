
from flask import Blueprint, request, jsonify
from app.models.database import db, AdminUser
from werkzeug.security import generate_password_hash, check_password_hash

admin = Blueprint('admin', __name__)

@admin.route('/api/admin/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])
    user = AdminUser(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Admin registered successfully'})

@admin.route('/api/admin/login', methods=['POST'])
def login():
    data = request.get_json()
    user = AdminUser.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

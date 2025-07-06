
from flask import Blueprint, request, jsonify
from app.utils.phishing_rules import is_phishing_url
from app.models.database import db, URLCheck

url_checker = Blueprint('url_checker', __name__)

@url_checker.route('/api/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url', '')
    result = is_phishing_url(url)
    url_check = URLCheck(url=url, is_phishing=result)
    db.session.add(url_check)
    db.session.commit()
    return jsonify({'url': url, 'is_phishing': result})

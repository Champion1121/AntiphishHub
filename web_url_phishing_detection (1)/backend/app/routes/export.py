
from flask import Blueprint, make_response
from app.models.database import db, URLCheck
import csv
import io

export = Blueprint('export', __name__)

@export.route('/api/export-logs', methods=['GET'])
def export_logs():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'URL', 'Is Phishing', 'Timestamp'])
    logs = URLCheck.query.all()
    for log in logs:
        writer.writerow([log.id, log.url, log.is_phishing, log.timestamp])
    output.seek(0)
    response = make_response(output.read())
    response.headers["Content-Disposition"] = "attachment; filename=url_logs.csv"
    response.headers["Content-type"] = "text/csv"
    return response

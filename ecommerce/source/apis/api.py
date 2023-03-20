from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'))

    def __init__(self, ip, city, state, country, url_id):
        self.ip = ip
        self.city = city
        self.state = state
        self.country = country
        self.url_id = url_id

    def serialize(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'created_at': self.created_at.isoformat(),
            'url_id': self.url_id
        }

@app.route('/visits', methods=['GET', 'POST'])
def visit_list():
    if request.method == 'GET':
        visits = Visit.query.all()
        return jsonify([visit.serialize() for visit in visits]), 200
    elif request.method == 'POST':
        ip = request.json['ip']
        city = request.json['city']
        state = request.json['state']
        country = request.json['country']
        url_id = request.json['url_id']
        visit = Visit(ip, city, state, country, url_id)
        db.session.add(visit)
        db.session.commit()
        return visit.serialize(), 201

@app.route('/visits/<int:visit_id>', methods=['GET', 'PUT', 'DELETE'])
def visit_detail(visit_id):
    visit = Visit.query.get_or_404(visit_id)
    if request.method == 'GET':
        return visit.serialize(), 200
    elif request.method == 'PUT':
        visit.ip = request.json.get('ip', visit.ip)
        visit.city = request.json.get('city', visit.city)
        visit.state = request.json.get('state', visit.state)
        visit.country = request.json.get('country', visit.country)
        visit.url_id = request.json.get('url_id', visit.url_id)
        db.session.commit()
        return visit

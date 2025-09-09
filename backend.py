from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///users.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ===== Model =====
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    disability = db.Column(db.String(50))

@app.before_first_request
def create_tables():
    db.create_all()

# ===== Register Account =====
@app.route('/register_account', methods=['POST'])
def register_account():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"user_id": user.id, "message": "Account created."})

# ===== Register Profile =====
@app.route('/register_profile', methods=['POST'])
def register_profile():
    data = request.json
    user_id = data.get("user_id")
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.dob = data.get("dob")
    user.weight = data.get("weight")
    user.height = data.get("height")
    user.disability = data.get("disability")
    db.session.commit()
    return jsonify({"message": "Profile completed", "user": {
        "username": user.username,
        "email": user.email,
        "dob": user.dob,
        "weight": user.weight,
        "height": user.height,
        "disability": user.disability
    }})

# ===== Recommendation =====
@app.route('/get_recommendation', methods=['POST'])
def recommendation():
    data = request.json
    ai_url = os.getenv("AI_SERVICE_URL", "https://your-ai-service.up.railway.app")
    try:
        res = requests.post(f"{ai_url}/recommendation", json=data)
        return jsonify(res.json())
    except:
        return jsonify({"error": "AI service failed"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

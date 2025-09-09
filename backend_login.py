from flask import Flask, request, jsonify

app = Flask(__name__)  # gunakan '=' bukan '=='

users = {}

@app.route('/register_account', methods=['POST'])
def register_account():
    data = request.json
    print(data)
    username = data.get("username")
    print(username)
    email = data.get("email")
    print(email)
    password = data.get("password")
    print(password)
    
    user_id = f"user_{len(users)+1:03d}"
    users[user_id] = {
        "username": username,
        "email": email,
        "password": password,
        "profile": {}
    }

    return jsonify({"user_id": user_id, "message": "Account created. Continue to profile registration."})


@app.route('/register_profile', methods=['POST'])
def register_profile():
    data = request.json
    user_id = data.get("user_id")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    # harus diindentasikan ke dalam fungsi
    users[user_id]["profile"] = {
        "dob": data.get("dob"),
        "weight": data.get("weight"),
        "height": data.get("height"),
        "disability": data.get("disability")
    }

    return jsonify({"message": "Profile completed", "user": users[user_id]})



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from rule_engine import rekomendasi_latihan, latihan

app = Flask(__name__)

@app.route("/rekomendasi", methods=["POST"])
def get_rekomendasi():
    user = request.json
    hasil = rekomendasi_latihan(user, latihan)
    print(hasil)
    return jsonify(hasil)

if __name__ == "__main__":
    app.run(debug=True)
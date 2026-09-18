from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "DevSecOps Production Service Running",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

# SIMULATED SECRET LEAK (TO TEST DEVSECOPS PIPELINE FAILURE)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEAKIAIOSFODNN7EXAMPLE"

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "DevSecOps Production Service Running",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    
import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return os.getenv("DB_PASS")
    # return 'Hello Devops2 production branch !'

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')

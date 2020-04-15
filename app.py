from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello Devops2 production branch !'

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

@app.route("/test-db")
def test_db():
    try:
        conn = psycopg2.connect(user = "devops2-user",
                                  password = "devops2",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "devops2")

        return "Database connected !"
    except Exception as error:
        return "Error connection to the database:" +  str(error)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

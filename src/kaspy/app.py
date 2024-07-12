from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def create_app():
    return app

@app.route("/")
def hello_world():
    return 'Hello, everyone ! ... hello Docker!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
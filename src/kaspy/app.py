from flask import Flask

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    @app.route("/")
    def index():
        return 'Hello, everyone ! ... hello Docker!'

    return app

# if __name__ == "__main__":
#    app.run(debug=True, host='0.0.0.0')
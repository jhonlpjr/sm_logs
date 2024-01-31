# main.py

from flask import Flask
from src.infraestructure.controllers.log_controller import log_bp

app = Flask(__name__)

app.register_blueprint(log_bp)

if __name__ == "__main__":
    app.run()
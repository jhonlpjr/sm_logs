import logging
from flask import Flask
from src.infraestructure.controllers.log_controller import log_bp

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    
    handler = Flask(__name__)

    logger.info(' Starting lambda ms-logs')

    handler.register_blueprint(log_bp)
    
    if __name__ == "__main__":
        handler.run()
        
except Exception as e:
    error_message = "main | Error: " + str(e)
    logger.error(f" {error_message}")
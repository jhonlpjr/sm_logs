import logging
from flask import Blueprint, jsonify, request

from marshmallow import ValidationError
from src.shared.enums.config_enum import CONFIG
from src.infraestructure.dto.request.find_logs_dto_req import FindLogsRequestDto
from src.infraestructure.dto.request.create_log_dto_req import CreateLogDtoReq

from src.application.usecases.create_log_usecase import CreateLogUsecase
from src.application.usecases.find_logs_usecase import FindLogsUsecase

# from src.application.usecases.find_one_log_usecase import FindOneLogUsecase

log_bp = Blueprint("log", __name__)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@log_bp.route("/log/test", methods=["GET"])
def test():
    # Lógica prueba
    try:
        #logger.info("log.controller:" + CONFIG.MONGO_URL)
        return jsonify({"message": "jola"}), 200
    except Exception as e:
        error_message = "log.controller | Error: " + str(e)
        logger.error(f" {error_message}")
        return jsonify({"error": error_message}), 500


@log_bp.route("/log/<string:collection_name>", methods=["POST"])
def save_log(collection_name):
    # llamando al caso de uso para crear logs
    try:
        # bodyRaw = json.loads(request.json)
        # body = SimpleNamespace(**bodyRaw)
        useCase = CreateLogUsecase(collection_name)
        reqBody = request.json
        dto = CreateLogDtoReq(reqBody)
        logger.info(" log_controller.save_log | request.body: " + str(reqBody))
        result = useCase.execute(dto)
        response = {"message": "Log created successfully", "data": result}
        return jsonify(response), 201
    except ValidationError as e:
        error_message = "log_controller.save_log | Error de validación: " + str(e)
        logger.error(f" {error_message}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = "log_controller.save_log | Error: " + str(e)
        logger.error(f" {error_message}")
        return jsonify({"error": error_message}), 500


@log_bp.route("/log/<string:collection_name>", methods=["GET"])
def get_logs(collection_name):
    # llamando al caso de uso para obtener logs
    try:
        useCase = FindLogsUsecase(collection_name)
        reqParams = request.args
        dto = FindLogsRequestDto(reqParams)
        logger.info("log_controller.save_log | request.params: " + str(reqParams))
        result = useCase.execute(dto.filter)
        response = {
            "message": "Logs found successfully",
            "data": result,
            "total": len(result),
            "collection": collection_name,
        }
        return jsonify(response), 200
    except ValidationError as e:
        error_message = "log_controller.get_logs | Error de validación: " + str(e)
        logger.error(f" {error_message}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = "log_controller.get_logs | Error: " + str(e)
        logger.error(f" {error_message}")
        return jsonify({"error": error_message}), 500


# @log_bp.route("/log/<string:collection_name>/<int:log_id>", methods=["GET"])
# def get_log(collection_name, log_id):
#     # llamando al caso de uso para obtener un log
#     useCase = FindOneLogUsecase(collection_name)
#     log = useCase.execute(log_id)
#     response = json.dumps(log.__dict__)
#     if response:
#         return response, 200
#     else:
#         return jsonify({"error": "Log not found"}), 404

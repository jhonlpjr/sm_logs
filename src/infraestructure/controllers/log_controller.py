import json
from flask import Blueprint, jsonify, request
from collections import namedtuple
from types import SimpleNamespace
from src.infraestructure.dto.request.create_log_dto_req import CreateLogDtoReq

from src.application.usecases.create_log_usecase import CreateLogUsecase
from src.application.usecases.find_logs_usecase import FindLogsUsecase
from src.application.usecases.find_one_log_usecase import FindOneLogUsecase

log_bp = Blueprint('log', __name__)

@log_bp.route('/log/test', methods=['GET'])
def test():
    # Lógica prueba

        return jsonify({'message': "jola"}), 200

@log_bp.route('/log/<string:collection_name>', methods=['POST'])
def save_log(collection_name):
    # llamando al caso de uso para crear logs
    try:
        useCase = CreateLogUsecase(collection_name)
        #bodyRaw = json.loads(request.json)
        #body = SimpleNamespace(**bodyRaw)
        dto = CreateLogDtoReq(request.json)
        log = useCase.execute(dto, 1)

        response = json.dumps(log.__dict__)
        #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>response", response)
        return response, 201
    
    except Exception as e:
        error_message = "Error de validación: " + str(e)
        return jsonify({'error': error_message}), 400

@log_bp.route('/log/<string:collection_name>', methods=['GET'])
def get_logs(collection_name):
    # llamando al caso de uso para obtener logs
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>acaaa", collection_name)
    useCase = FindLogsUsecase(collection_name)
    data = request.args
    log = useCase.execute(data)
    if log:
        return jsonify(log), 200
    else:
        return jsonify({'error': 'Logs not found'}), 404

@log_bp.route('/log/<string:collection>/<int:log_id>', methods=['GET'])
def get_log(collection_name, log_id):
    # llamando al caso de uso para obtener un log
    useCase = FindOneLogUsecase(collection_name)
    log = useCase.execute(log_id)
    if log:
        return jsonify(log), 200
    else:
        return jsonify({'error': 'Log not found'}), 404
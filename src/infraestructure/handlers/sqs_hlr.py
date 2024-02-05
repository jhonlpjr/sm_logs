import json
import logging
from marshmallow import ValidationError
from src.infraestructure.dto.request.create_log_dto_req import CreateLogDtoReq
from src.application.usecases.create_log_usecase import CreateLogUsecase
from src.infraestructure.controllers.log_controller import save_log

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def save_log_handler(event, context):
    try:
        logger.info(" Message for sqs ms-save-log")

        for record in event["Records"]:
            # El cuerpo del mensaje se encuentra en 'body'
            logger.info(" Record" + str(record))
            msg_body = json.loads(record["body"])
            msg_collection = msg_body["collection"]
            msg_dto = msg_body["dto"]
            # Aquí puedes pasar message_body a tu caso de uso
            # Por ejemplo:
            useCase = CreateLogUsecase(msg_collection)
            dto = CreateLogDtoReq(msg_dto)
            logger.info(" sqs_hlr.save_log_handler | msg_collection: " + msg_collection)
            logger.info(" sqs_hlr.save_log_handler | msg_dto: " + str(msg_dto))
            result = useCase.execute(dto)
            response = {"message": "Log created successfully", "data": result}
            logger.info("response:", str(response))

    except ValidationError as e:
        error_message = "sqs_hlr.save_log_handler | Error de validación: " + str(e)
        logger.error(f" {error_message}")

    except Exception as e:
        error_message = "sqs_hlr.save_log_handler | Error: " + str(e)
        logger.error(f" {error_message}")


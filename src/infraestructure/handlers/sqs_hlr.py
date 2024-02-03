import json
import logging
from marshmallow import ValidationError
from infraestructure.dto.request.create_log_dto_req import CreateLogDtoReq
from src.application.usecases.create_log_usecase import CreateLogUsecase
from src.infraestructure.controllers.log_controller import save_log

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def save_log_handler(event, context):
    try:
        logger.info(" Message for sqs ms-save-log")
        for record in event["Records"]:
            # El cuerpo del mensaje se encuentra en 'body'
            msg_body = json.loads["body"]
            msg_collection = record["collection"]
            # Aquí puedes pasar message_body a tu caso de uso
            # Por ejemplo:
            useCase = CreateLogUsecase(msg_collection)
            dto = CreateLogDtoReq(msg_body)
            logger.info(" sqs_hlr.save_log_handler | msg_collection: " + msg_collection)
            logger.info(" sqs_hlr.save_log_handler | msg_body: " + str(msg_body))
            result = useCase.execute(dto, 1)
            response = {"message": "Log created successfully", "data": result}
            logger.info("response:", response)

    except ValidationError as e:
        error_message = "sqs_hlr.save_log_handler | Error de validación: " + str(e)
        logger.error(f" {error_message}")

    except Exception as e:
        error_message = "sqs_hlr.save_log_handler | Error: " + str(e)
        logger.error(f" {error_message}")


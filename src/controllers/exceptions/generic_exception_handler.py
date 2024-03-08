from fastapi import HTTPException, status
from pymongo.errors import OperationFailure
from ...services.service_exceptions import (
ServiceLayerDuplicateError,
ServiceLayerNoneError,
ServiceLayerGeneralError,
ServiceLayerPermissionError
)

exceptions_case = {
    ServiceLayerDuplicateError: status.HTTP_400_BAD_REQUEST,
    ServiceLayerNoneError: status.HTTP_404_NOT_FOUND,
    ServiceLayerGeneralError: status.HTTP_400_BAD_REQUEST,
    ServiceLayerPermissionError: status.HTTP_403_FORBIDDEN,
    OperationFailure: status.HTTP_400_BAD_REQUEST
}

class GenericExceptionHandlerController:

    @staticmethod
    def execute(ex):
        status_code = exceptions_case.get(type(ex))
        if status_code:
            raise HTTPException(detail=str(ex), status_code=status_code)

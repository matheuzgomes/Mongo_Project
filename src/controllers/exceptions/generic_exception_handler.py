from dataclasses import dataclass
from fastapi import HTTPException, status
from ...services.service_exceptions import ServiceLayerDuplicateError, ServiceLayerNoneError


@dataclass
class GenericExceptionHandlerController():
    @staticmethod
    def execute(ex: Exception):
        if isinstance(ex, ServiceLayerDuplicateError):
            raise HTTPException(detail=str(ex), status_code=status.HTTP_400_BAD_REQUEST)
        
        if isinstance(ex, ServiceLayerNoneError):
            raise HTTPException(detail=str(ex), status_code=status.HTTP_404_NOT_FOUND)

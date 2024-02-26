class ServiceLayerGeneralError(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if condition:
            raise ServiceLayerGeneralError(message)

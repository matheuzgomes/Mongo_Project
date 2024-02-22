class ServiceLayerDuplicateError(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if condition:
            raise ServiceLayerDuplicateError(message)

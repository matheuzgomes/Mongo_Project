class ServiceLayerPermissionError(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if condition:
            raise ServiceLayerPermissionError(message)

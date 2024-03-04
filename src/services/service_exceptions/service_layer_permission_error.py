class ServiceLayerPermissionError(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if not condition:
            raise ServiceLayerPermissionError(message)

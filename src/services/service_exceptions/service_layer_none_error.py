class ServiceLayerNoneError(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if condition:
            raise ServiceLayerNoneError(message)

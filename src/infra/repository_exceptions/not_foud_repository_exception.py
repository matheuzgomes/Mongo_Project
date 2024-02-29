class NotFoundException(Exception):
    @staticmethod
    def when(condition: bool, message:str):
        if condition:
            raise NotFoundException(message)
from dataclasses import dataclass
import os

@dataclass
class WebappSettings():
    project_name = 'Task Manager'
    environment = ""
    version = '0.0.1'
    debug: bool = True
    host: str = "127.0.0.1"

    def __init__(self):
        enviroment = os.environ.get('STAGE', "")
        self.environment = enviroment.upper()

    @property
    def title(self) -> str:
        if (self.environment):
            return f'{self.project_name} ({self.environment})'

        return self.project_name

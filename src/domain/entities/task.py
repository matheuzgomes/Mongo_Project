from dataclasses import dataclass

@dataclass
class Task:
    _id:int = 0 
    task_name: str = ""
    task_status: str = ""
    description: str = ""
    
    def validate_fields(self):
        if not isinstance(self.task_name, str):
            raise TypeError(f"{self.task_name} is not an string")
        if not isinstance(self.task_status, str):
            raise TypeError(f"{self.task_status} is not an string")
        if len(self.description) > 500:
            raise ValueError(f"{self.description} has too many characters")

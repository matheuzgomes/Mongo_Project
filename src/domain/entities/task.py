from dataclasses import dataclass

@dataclass
class Task:
    task_name: str
    _id:int = 0
    task_status: str = ""
    description: str = ""
    is_active:bool = True
    user_id:int = 0
    
    def validate_fields(self):
        if not isinstance(self.task_name, str):
            raise TypeError(f"{self.task_name} is not an string")
        if not isinstance(self.task_status, str):
            raise TypeError(f"{self.task_status} is not an string")
        if not isinstance(self.user_id, int):
            raise TypeError("Invalid user id")
        if len(self.description) > 5000:
            raise ValueError(f"{self.description} has too many characters")

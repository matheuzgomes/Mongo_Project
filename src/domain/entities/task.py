from typing import List
from dataclasses import dataclass, field


@dataclass
class Task:
    task_name: str
    _id:int = 0
    task_status: str = ""
    description: str = ""
    is_active:bool = True
    user_id:int = 0
    tags: List[str] = field(default_factory=[""])
    
    def validate_fields(self):
        self.validate_field_type(self.task_name, str, f"{self.task_name} is not a string")
        self.validate_field_type(self.task_status, str, f"{self.task_status} is not a string")
        self.validate_field_type(self.user_id, int, "Invalid user id")
        self.validate_description_length()

    def validate_field_type(self, field, field_type, error_message):
        if not isinstance(field, field_type):
            raise TypeError(error_message)

    def validate_description_length(self):
        if len(self.description) > 5000:
            raise ValueError(f"{self.description} has too many characters")

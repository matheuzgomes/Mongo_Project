from dataclasses import dataclass


@dataclass
class User:
    user_id:int = 0
    username: str = ""
    password : str = ""
    name:str = ""
    description:str = ""
    is_active:bool = True
    active_tasks:int = 0
    task_limit:int = 0

    def validate_fields(self):
        self.validate_field_type(self.user_id, int, "Invalid Id")
        self.validate_field_type(self.username, str, "Invalid username")
        self.validate_field_type(self.password, str, "Invalid password")
        self.validate_field_type(self.name, str, f"Invalid User Name => {self.name}")
        self.validate_field_type(self.description, str, "Invalid user description")
        self.validate_field_type(self.is_active, bool, "Invalid active information")
        self.validate_field_type(self.active_tasks, int, "Invalid task number")
        self.validate_field_type(self.task_limit, int, "Invalid task limit")

    def validate_field_type(self, field, field_type, error_message):
        if not isinstance(field, field_type):
            raise TypeError(error_message)

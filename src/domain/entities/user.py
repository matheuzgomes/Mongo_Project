from dataclasses import dataclass


@dataclass
class User:
    _id:int = 0
    username: str = ""
    password : str = ""
    name:str = ""
    description:str = ""
    is_active:bool = True
    active_tasks:int = 0
    task_limit:int = 0


    def validate_fields(self):
        if not  isinstance(self._id, int):
            raise TypeError("Invalid Id")
        if not  isinstance(self.username, str):
            raise TypeError("Invalid username")
        if not  isinstance(self.password, str):
            raise TypeError("Invalid password")
        if not isinstance(self.name, str):
            raise TypeError(f"Invalid Name => {self.name}")
        if not isinstance(self.description, str):
            raise TypeError("Invalid user description")
        if not isinstance(self.is_active, bool):
            raise TypeError("Invalid active information")
        if not isinstance(self.active_tasks, int):
            raise TypeError("Invalid task number")
        if not isinstance(self.task_limit, int):
            raise TypeError("Invalid task limit")

from dataclasses import dataclass


@dataclass
class User:
    _id:int = 0
    name:str = ""
    description:str = ""
    is_active:bool = ""
    active_tasks:int = ""
    task_limit:int = ""


    def validate_data(self):
        if not  isinstance(self._id, int):
            raise TypeError("Invalid Id")
        if not isinstance(self.name, str):
            raise TypeError(f"Invalid User Name => {self.name}")
        if not isinstance(self.description, str):
            raise TypeError("Invalid user description")
        if not isinstance(self.is_active, bool):
            raise TypeError("Invalid active information")
        if not isinstance(self.active_tasks, int):
            raise TypeError("Invalid task number")
        if not isinstance(self.task_limit, int):
            raise TypeError("Invalid task limit")
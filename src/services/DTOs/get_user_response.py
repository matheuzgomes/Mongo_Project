from dataclasses import dataclass

@dataclass
class GetUserResponse:
    _id:int
    username: str
    password : str
    name:str
    description:str
    is_active:bool
    active_tasks:int
    task_limit:int
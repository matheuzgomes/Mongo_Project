from dataclasses import dataclass

@dataclass
class GetUserResponse:
    id:int
    user_id:int
    username: str
    name:str
    description:str
    is_active:bool
    active_tasks:int
    task_limit:int
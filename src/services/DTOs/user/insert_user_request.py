from pydantic import BaseModel

class InsertUserRequest(BaseModel):
    username: str
    password : str
    name:str
    description:str
    is_active:bool = True
    active_tasks:int = 0
    task_limit:int = 10

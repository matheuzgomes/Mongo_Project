from pydantic import BaseModel
from typing import List


class InsertUserBaseModel(BaseModel):
    username: str
    password : str
    name:str
    description:str
    is_active:bool = True
    active_tasks:int = 0
    task_limit:int = 10
    scopes:List[str] = None

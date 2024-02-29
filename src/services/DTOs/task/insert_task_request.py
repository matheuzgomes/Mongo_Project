from typing import List
from pydantic import BaseModel

class InsertTaskRequest(BaseModel):
    task_name: str
    task_status: str 
    description: str 
    is_active: bool 
    tags: List[str] = None

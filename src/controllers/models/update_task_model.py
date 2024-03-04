from typing import List, Optional
from pydantic import BaseModel

class UpdateTaskRequest(BaseModel):
    task_name: str = ""
    task_status: str = ""
    description: str = ""
    is_active:bool = True
    tags: Optional[List[str]] = None
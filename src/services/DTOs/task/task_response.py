from typing import List
from dataclasses import dataclass

@dataclass
class TasksForResponse:
    id:int
    task_name: str
    task_status: str
    description: str
    tags: List[str]

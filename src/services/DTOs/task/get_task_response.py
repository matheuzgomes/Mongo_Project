from typing import Dict
from dataclasses import dataclass

@dataclass
class GetTaskResponse:
    id:int
    task_name: str
    task_status: str
    info: Dict[str, str]

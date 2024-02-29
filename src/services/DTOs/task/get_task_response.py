from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class GetTaskResponse:
    id: int
    user_id: int
    task_name: str
    task_status: str
    info: Dict[str, Any]

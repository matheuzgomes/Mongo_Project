from dataclasses import dataclass


@dataclass
class TasksForResponse:
    _id:int
    task_name: str
    task_status: str
    description: str
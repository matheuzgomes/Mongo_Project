from dataclasses import dataclass


@dataclass
class InsertTaskRequest:
    task_name: str = None
    task_status: str = None
    description: str = None
from typing import List
from .task_response import TasksForResponse

class ListTaskResponse:
    def __init__(self, data: List[TasksForResponse], count:int) -> None:
        self.count = count
        self.data = data
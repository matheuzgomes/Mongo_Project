from abc import abstractmethod
from typing import Any
from ...domain.entities import Task

class ITaskRepository():

    @abstractmethod
    def find_all(self) -> Any:
        raise Exception("Not Implemented")

    @abstractmethod
    def find_one(self, task_id:int) -> Task:
        raise Exception("Not Implemented")


    @abstractmethod
    def insert(self, document: Task) -> Any:
        raise Exception("Not Implemented")

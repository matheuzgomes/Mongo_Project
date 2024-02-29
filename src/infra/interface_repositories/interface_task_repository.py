from abc import abstractmethod
from typing import Any, Dict
from ...domain.entities import Task

class ITaskRepository():

    @abstractmethod
    async def find_all(self) -> Any:
        raise Exception("Not Implemented")

    @abstractmethod
    async def find_one(self, task_id:int) -> Task:
        raise Exception("Not Implemented")

    @abstractmethod
    async def insert(self, document: Task) -> Any:
        raise Exception("Not Implemented")
    
    @abstractmethod
    async def delete(self, id:int = None, batch_delete: Dict[str, Any] = None) -> None:
        raise Exception("Not Implemented")

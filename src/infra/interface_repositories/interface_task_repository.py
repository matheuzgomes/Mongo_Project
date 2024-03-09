from abc import abstractmethod
from typing import Any, Dict
from ...domain.entities import Task

class ITaskRepository():

    @abstractmethod
    async def find_all_by_user_id(self, user_id:int) -> Any:
        raise Exception("Not Implemented")

    @abstractmethod
    async def find_one_by_id(self, task_id:int, user_id:int) -> Task:
        raise Exception("Not Implemented")

    @abstractmethod
    async def find_one_by_generic_string_field(self, search_field: str, user_id:int, value_searched:str) -> Task:
        raise Exception("Not Implemented")

    @abstractmethod
    async def insert(self, document: Task) -> Any:
        raise Exception("Not Implemented")

    @abstractmethod    
    async def update(self, query_find: Dict[str, Any], query_update: Dict[str, Any]):
        raise Exception("Not Implemented")

    @abstractmethod
    async def delete(self, id:int = None, batch_delete: Dict[str, Any] = None) -> None:
        raise Exception("Not Implemented")

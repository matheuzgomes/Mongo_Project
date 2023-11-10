from abc import abstractmethod
from typing import Any
from ..domain.entities import Task

class IRepository():

    @abstractmethod
    def find_all(self) -> Any:
        raise Exception("Not Implemented")
    
    @abstractmethod
    def insert(self, document: Task) -> Any:
        raise Exception("Not Implemented")
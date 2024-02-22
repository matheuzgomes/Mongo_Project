from abc import abstractmethod
from typing import Any
from ...domain.entities import User

class IUserRepository:

    @abstractmethod
    def find_all(self) -> Any:
        raise Exception("Not Implemented")
    
    @abstractmethod    
    def find_one(self, user_id: int) -> Any:
        raise Exception("Not Implemented")
    
    @abstractmethod
    def find_one_by_name(self, field: str, data:str) -> User:
        raise Exception("Not Implemented")
    
    @abstractmethod
    def insert(self, document: User) -> Any:
        raise Exception("Not Implemented")
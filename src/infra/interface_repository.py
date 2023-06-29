from abc import abstractmethod
from typing import Any

class IRepository:

    @abstractmethod
    def find_all() -> Any:
        raise Exception("Not Implemented")
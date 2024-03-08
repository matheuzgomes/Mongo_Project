from abc import abstractmethod
from typing import Any
from ...domain.entities import Log

class ILogRepository():

    @abstractmethod
    async def insert(self, document: Log) -> Any:
        raise Exception("Not Implemented")

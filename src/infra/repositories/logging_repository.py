from src.domain.entities import Log
from ..interface_repositories import ITaskRepository
from ..db_handler import DbHandler
from .utils.counter_db import CounterDB


class LogRepository(ITaskRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = self.db.logs

    async def insert(self, document: Log) -> None:
        document.validate_fields()
        document._id = CounterDB.counter(self.db.counter_for_logs).inserted_id
        self.collection.insert_one(document.__dict__)
        return

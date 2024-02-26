from typing import List
from src.domain.entities import Task
from ..interface_repositories import ITaskRepository
from ..db_handler import DbHandler
from .utils.counter_db import CounterDB


class TaskRepository(ITaskRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = self.db.Task

    def find_all(self) -> List[Task]:
        return self.collection.count_documents({}), self.collection.find()

    def find_one(self, task_id:int) -> Task:
        return self.collection.find_one({"_id": task_id})

    def insert(self, document: Task) -> None:
        document.validate_fields()
        document._id = CounterDB.counter(self.db.counter_for_task).inserted_id
        result = self.collection.insert_one(document.__dict__)
        return str(result.inserted_id)

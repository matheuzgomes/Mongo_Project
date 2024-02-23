from pymongo import DESCENDING
from typing import List
from src.domain.entities import Task
from ..interface_repositories import ITaskRepository
from ..db_handler import DbHandler


class TaskRepository(ITaskRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = self.db.Task

    def find_all(self) -> List[Task]:
        return self.collection.count_documents({}), self.collection.find()

    def find_one(self, task_id:int) -> Task:
        return self.collection.find_one({"task_id": task_id})

    def insert(self, document: Task) -> None:
        document.validate_fields()
        document._id = self.counter_for_task().inserted_id
        result = self.collection.insert_one(document.__dict__)
        return str(result.inserted_id)

    def counter_for_task(self) -> None:
        connection = self.db.counter_for_task
        id = connection.find_one(sort=[('counter_id', DESCENDING)])
        counter = connection.insert_one({"counter_id": id['counter_id'] + 1})
        return counter

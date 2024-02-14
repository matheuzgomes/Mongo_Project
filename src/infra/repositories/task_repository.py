from pymongo import DESCENDING
from src.domain.entities import Task
from ..interface_repositories import ITaskRepository
from ..db_handler import DbHandler


class TaskRepository(ITaskRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = db.collection

    def find_all(self) -> Task:
        return self.collection.count_documents({}), self.collection.find()
    
    def find_one(self, task_id) -> Task:
        return self.collection.find_one({"_id": task_id})

    def insert(self, document: Task) -> None:
        document.validate_fields()
        document._id = self.counter_for_task().inserted_id
        result = self.collection.insert_one(document.__dict__)
        return str(result.inserted_id)

    def counter_for_task(self) -> None:
        connection = self.db.counter_for_task
        id = connection.find_one(sort=[('_id', DESCENDING)])
        counter = connection.insert_one({"_id": id['_id'] + 1})
        return counter

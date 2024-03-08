from typing import List, Dict, Any
from src.domain.entities import Task
from ..interface_repositories import ITaskRepository
from ..db_handler import DbHandler
from .utils.counter_db import CounterDB
from ..repository_exceptions import NotFoundException


class TaskRepository(ITaskRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = self.db.Task

    async def find_all_by_user_id(self, user_id:int) -> List[Task]:
        return self.collection.count_documents({}), self.collection.find({"user_id": user_id})

    async def find_one_by_id(self, task_id:int, user_id:int) -> Task:
        return self.collection.find_one(
            {"$and":[
                {"_id": task_id},
                {"user_id": user_id}
                ]})

    async def find_one_by_generic_string_field(self, search_field: str, value_searched:str) -> Task:
        return self.collection.find_one({f"{search_field}": f"{value_searched}"})

    async def insert(self, document: Task) -> None:
        document.validate_fields()
        document._id = CounterDB.counter(self.db.counter_for_task).inserted_id
        self.collection.insert_one(document.__dict__)
        return

    async def update(self, query_find: Dict[str, Any], query_update: Dict[str, Any]):
        return self.collection.update_one(query_find, query_update)

    async def delete(self, id:int = None, batch_delete: Dict[str, Any] = None) -> int:
        NotFoundException.when(id is None and batch_delete is None, "Not found any document")

        if id:
            return self.collection.delete_one({"_id": id}).deleted_count

        elif batch_delete:
            for document in batch_delete.items():
                return self.collection.delete_many({f"{document[0]}": document[1]}).deleted_count

from typing import List
from src.domain.entities import User
from ..interface_repositories import IUserRepository
from ..db_handler import DbHandler
from .utils.counter_db import CounterDB


class UserRepository(IUserRepository):
    def __init__(self, db: DbHandler) -> None:
        self.db = db.database
        self.collection = self.db.User

    def find_all(self) -> List[User]:
        return self.collection.count_documents({}), self.collection.find()

    def find_one_by_id(self, user_id: int) -> User:
        return self.collection.find_one({"_id": user_id})

    def find_one_by_name(self, field: str, data:str) -> User:
        return self.collection.find_one({f"{field}": data})

    def insert(self, document: User) -> None:
        document.validate_fields()
        document._id = CounterDB.counter(self.db.counter_for_user).inserted_id
        result = self.collection.insert_one(document.__dict__)
        return str(result.inserted_id)

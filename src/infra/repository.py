import os
from pymongo import MongoClient, DESCENDING
from dotenv import load_dotenv
from src.domain.entities import Task
from .interface_repository import IRepository


class MongoRepository(IRepository):
    def __init__(self) -> None:
        load_dotenv()
        self.client = MongoClient(os.getenv('CONNECTION_STRING'))
        self.db = self.client[os.getenv('BANK_NAME')]
        self.collection = self.db[os.getenv('COLLECTION_NAME')]

    def find_all(self) -> Task:
        return self.collection.find()

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

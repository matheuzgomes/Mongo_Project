from typing import Dict
from pymongo import MongoClient
from dotenv import load_dotenv
from src.domain.entities import Task
from .interface_repository import IRepository
import os


class MongoRepository(IRepository):
    def __init__(self) -> None:
        load_dotenv()
        self.client = MongoClient(os.getenv('CONNECTION_STRING'))
        self.db = self.client[os.getenv('BANK_NAME')]
        self.collection = self.db[os.getenv('COLLECTION_NAME')]


    def find_all(self) -> Dict[Task]:
        return self.collection.find()

    def insert(self, document: Task) -> None:
        document.validate_fields()
        result = self.collection.insert_one(document.to_dict())
        return str(result.inserted_id)
    

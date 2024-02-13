import os
from pymongo import MongoClient

class DbHandler:
    def __init__(self) -> None:
        self.client = MongoClient(os.getenv('CONNECTION_STRING'))
        self.database = self.client[os.getenv('BANK_NAME')]
        self.collection = self.database[os.getenv('COLLECTION_NAME')]

import os
from pymongo import MongoClient

class DbHandler:

    def __init__(self) -> None:
        self.client = MongoClient(os.environ.get('CONNECTION_STRING'))
        self.database = self.client[os.environ.get('BANK_NAME')]

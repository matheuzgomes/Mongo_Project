from pymongo import DESCENDING

class CounterDB:

    def __init__(self, collection: str) -> None:
         self.collection = collection

    def counter(self):
        id = self.collection.find_one(sort=[('_id', DESCENDING)])
        counter = self.collection.insert_one({"_id": id['_id'] + 1})
        return counter
    
    def counter_for_task(self) -> None:
        connection = self.db.counter_for_task
        id = connection.find_one(sort=[('_id', DESCENDING)])
        counter = connection.insert_one({"_id": id['_id'] + 1})
        return counter

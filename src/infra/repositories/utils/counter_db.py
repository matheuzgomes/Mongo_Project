from pymongo import DESCENDING

class CounterDB:

    @staticmethod
    def counter(db) -> None:
        connection = db
        id = connection.find_one(sort=[('_id', DESCENDING)])
        counter = connection.insert_one({"_id": id['_id'] + 1})
        return counter

from pymongo import DESCENDING

class CounterDB:

    @staticmethod
    def counter(db) -> None:

        try:

            connection = db
            id = connection.find_one(sort=[('_id', DESCENDING)])
            counter = connection.insert_one({"_id": id['_id'] + 1})

        except Exception as e:

            if isinstance(e, TypeError):
                connection.insert_one({"_id": 0})
                retry_id = connection.find_one(sort=[('_id', DESCENDING)])
                counter = connection.insert_one({"_id": retry_id['_id'] + 1})

                return counter
   
        return counter

from infra.repository import MongoRepository
from src.domain.entities import Task

# item_1 = {
#   "_id" : "U1IT00003",
#   "item_name" : "Accio",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020GRG",
#   "price" : 340,
#   "category" : "kitchen"
# }



# item = Task(10, "Expeliarmus", "Created", "testing")


item_ = Task(
             task_name="teste",
             task_status="created",
             description="teste"
             )

MongoRepository().insert(document=item_)
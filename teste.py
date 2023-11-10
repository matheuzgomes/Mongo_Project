import json
from src.services.get_all_tasks import GetAllTasksService
from src.services.insert_task import InsertTasksService
from src.infra.repository import MongoRepository
from src.services.DTOs import InsertTaskRequest
from uuid import uuid4


# data = InsertTaskRequest(task_name= "Criacao de items 2",
#                          task_status= "Done",
#                          description="Task completa")


# InsertTasksService.insert_tasks(MongoRepository(), data=data)

# item = GetAllTasksService.get_all(repo=MongoRepository())
# item
# json_dump = json.dumps({"data": item})

# print(json_dump)

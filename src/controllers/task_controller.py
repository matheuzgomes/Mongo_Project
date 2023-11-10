from fastapi import APIRouter
from ..services.insert_task import InsertTasksService
from ..infra.repository import MongoRepository
from ..services.DTOs import InsertTaskRequest

task_route = APIRouter()


@task_route.post("/")
def insert_task_controller(data: InsertTaskRequest):

    insert_data = InsertTaskRequest(task_name=data.task_name,
                                   task_status=data.task_status,
                                   description=data.description)
    

    try:
        data = InsertTasksService.insert_tasks(MongoRepository(), data=insert_data)


    except Exception as error:
        raise Exception(error)

    return data



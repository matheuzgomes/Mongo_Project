from fastapi import APIRouter
from ..services.insert_task import InsertTasksService
from ..services.get_all_tasks import GetAllTasksService
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



@task_route.get("/list")
def get_all_tasks_controller():
    try:
        data = GetAllTasksService.get_all(MongoRepository())

    except Exception as error:
        raise Exception(error) from error
    
    return data


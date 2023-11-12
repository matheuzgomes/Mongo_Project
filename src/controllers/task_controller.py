from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from ..services.insert_task import InsertTasksService
from ..services.get_all_tasks import GetAllTasksService
from ..infra.repositories import TaskRepository
from ..services.DTOs import InsertTaskRequest

task_route = APIRouter()
task_router = InferringRouter()

@cbv(task_router)
class Taskontroller():
    @task_route.post("/")
    def insert_task_controller(data: InsertTaskRequest):

        insert_data = InsertTaskRequest(task_name=data.task_name,
                                    task_status=data.task_status,
                                    description=data.description)
        

        try:
            data = InsertTasksService.insert_tasks(TaskRepository(), data=insert_data)


        except Exception as error:
            raise Exception(error)

        return JSONResponse(content=jsonable_encoder(data.__dict__))



    @task_route.get("/list")
    def get_all_tasks_controller():
        try:
            data = GetAllTasksService.get_all(TaskRepository())

        except Exception as error:
            raise Exception(error) from error
        
        return JSONResponse(content=jsonable_encoder(data.__dict__))

task_route.include_router(task_router)
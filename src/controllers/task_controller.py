from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from  typing import List
from ..services.DTOs.task.get_task_response import GetTaskResponse
from ..services.task.insert_task_service import InsertTasksService
from ..services.task.get_all_tasks_service import GetAllTasksService
from ..services.task.get_task_service import GetTaskService
from ..infra.repositories import TaskRepository
from ..services.DTOs.task import InsertTaskRequest
from ..infra.db_handler import DbHandler
from .exceptions import GenericExceptionHandlerController
from ..utils import CheckCurrentUser

task_route = APIRouter()
task_router = InferringRouter()

@cbv(task_router)
class Taskcontroller(DbHandler):

    def __init__(self) -> None:
        super().__init__()
        self.db = DbHandler()

    @task_router.post("/", description="Endpoint to create a new task")
    def insert_task_controller(self, data: InsertTaskRequest, user_token = Depends(CheckCurrentUser.get_current_user)):

        insert_data = InsertTaskRequest(
            task_name=data.task_name,
            task_status=data.task_status,
            description=data.description,
            is_active=data.is_active,
            user_id=data.user_id,
            tags=data.tags
            )

        try:
            data = InsertTasksService.insert_tasks(
                TaskRepository(self.db),
                data=insert_data
                )

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error

        return ""

    @task_router.get("/list", response_model=List[GetTaskResponse])
    def get_all_tasks_controller(self, user_token = Depends(CheckCurrentUser.get_current_user)):

        try:
            data = GetAllTasksService.get_all(TaskRepository(self.db))

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))

    @task_router.get("/{id}")
    def get_task(self, id:int, user_token = Depends(CheckCurrentUser.get_current_user)):

        try:
            data = GetTaskService.get(
                repo=TaskRepository(self.db),
                id=id
                )
        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))

task_route.include_router(task_router)

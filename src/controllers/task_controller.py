from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from  typing import List
from ..services.DTOs.task import (
    GetTaskResponse,
    DeleteDocumentRequest,
    DeleteDocumentCountResponse,
    InsertTaskRequest
)
from ..services.task import (
    InsertTasksService,
    GetAllTasksService,
    GetTaskService,
    DeleteTaskService
)
from ..infra.repositories import TaskRepository
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
    async def insert_task_controller(self, data: InsertTaskRequest, user_token = Depends(CheckCurrentUser.get_current_user)):

        insert_data = InsertTaskRequest(
            task_name=data.task_name,
            task_status=data.task_status,
            description=data.description,
            is_active=data.is_active,
            tags=data.tags
            )

        try:
            data = await InsertTasksService.insert_tasks(
                TaskRepository(self.db),
                data=insert_data,
                _user_token=user_token
                )

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error

        return ""

    @task_router.get("/list", response_model=List[GetTaskResponse])
    async def get_all_tasks_controller(self, user_token = Depends(CheckCurrentUser.get_current_user)):

        try:
            data = await GetAllTasksService.get_all(TaskRepository(self.db))

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))

    @task_router.get("/{id}")
    async def get_task(self, id:int, user_token = Depends(CheckCurrentUser.get_current_user)):

        try:
            data = await GetTaskService.get(
                repo=TaskRepository(self.db),
                id=id
                )
        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))
    
    @task_router.delete("/", response_model=DeleteDocumentCountResponse)
    async def delete_task(self, delete_data:DeleteDocumentRequest, user_token = Depends(CheckCurrentUser.get_current_user)):

        try:
            data = await DeleteTaskService.delete(
                repo=TaskRepository(self.db),
                id=delete_data.id,
                batch_delete=delete_data.batch_delete
                )

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))

task_route.include_router(task_router)

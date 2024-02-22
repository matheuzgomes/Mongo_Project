from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from  typing import List
from ..services.insert_user import InsertUserService
from ..services.get_all_users import GetAllUsersService
from ..infra.repositories import UserRepository
from ..services.DTOs import InsertUserRequest
from ..services.DTOs import GetUserResponse
from ..infra.db_handler import DbHandler

user_route = APIRouter()
user_router = InferringRouter()

@cbv(user_router)
class Taskcontroller(DbHandler):

    def __init__(self) -> None:
        super().__init__()
        self.db = DbHandler()

    @user_router.post("/", description="Endpoint to create a new User")
    def insert_task_controller(self, data: InsertUserRequest):

        insert_data = InsertUserRequest(
            username = data.username,
            password = data.password,
            name = data.name,
            description = data.description,
            )

        try:
            data = InsertUserService.insert_user(
                UserRepository(self.db),
                data=insert_data
                )

        except Exception as error:
            raise Exception(error)

        return ""

    @user_router.get("/list", response_model=List[GetUserResponse], description="Retrive all the disponible users")
    def get_all_tasks_controller(self):
        try:
            data = GetAllUsersService.get_all(UserRepository(self.db))

        except Exception as error:
            raise Exception(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))


user_route.include_router(user_router)
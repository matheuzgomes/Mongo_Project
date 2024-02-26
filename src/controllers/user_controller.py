from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from  typing import List
from ..services.user import (
    InsertUserService,
    GetAllUsersService,
    GetUserForLoginService
    )
from .exceptions import GenericExceptionHandlerController
from ..infra.repositories import UserRepository
from ..services.DTOs.user import InsertUserRequest
from ..services.DTOs.user import GetUserResponse
from ..infra.db_handler import DbHandler

user_route = APIRouter()
user_router = InferringRouter()

@cbv(user_router)
class Taskcontroller(DbHandler):

    def __init__(self) -> None:
        super().__init__()
        self.db = DbHandler()

    @user_router.post("/register", description="Endpoint to create a new User")
    def insert_user_controller(self, data: InsertUserRequest):

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
            raise GenericExceptionHandlerController.execute(error) from error

        return ""

    @user_router.get("/list", response_model=List[GetUserResponse], description="Retrive all the disponible users")
    def get_all_users_controller(self):
        try:
            data = GetAllUsersService.get_all(UserRepository(self.db))

        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=jsonable_encoder(data))

    @user_router.post('/login', summary="Create access and refresh tokens for user")
    def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        try:
            data = GetUserForLoginService.user_login(
                repo=UserRepository(self.db),
                data=form_data
                )
        except Exception as error:
            raise GenericExceptionHandlerController.execute(error) from error
        
        return JSONResponse(content=data)
        

user_route.include_router(user_router)
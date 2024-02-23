from typing import Dict
from fastapi import HTTPException, status
from ...infra.interface_repositories import IUserRepository
from ..service_exceptions import ServiceLayerNoneError
from ..DTOs.user import GetUserForLogin
from ...utils import UserAuthentication

class GetUserForLoginService:

    @staticmethod
    def user_login(
        repo:IUserRepository,
        data: GetUserForLogin
        ) -> Dict[str, str]:


        user_data = repo.find_one_by_name("username", data.username)
        ServiceLayerNoneError.when(
            user_data is None, "Incorret username or password"
        )

        hashed_pass = user_data['password']

        if not UserAuthentication().verify_password(data.password, hashed_pass):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorret username or password"
            )
        return {
            "access_token": UserAuthentication().create_access_token(user_data['username']),
            "refresh_token": UserAuthentication().create_refresh_token(user_data['username'])
        }

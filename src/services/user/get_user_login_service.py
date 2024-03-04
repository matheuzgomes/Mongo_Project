from typing import Dict
from ...infra.interface_repositories import IUserRepository
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerGeneralError, ServiceLayerPermissionError
from ..DTOs.user import GetUserForLogin
from ...utils import UserAuthentication

class GetUserForLoginService:

    @staticmethod
    async def user_login(
        repo:IUserRepository,
        data: GetUserForLogin
        ) -> Dict[str, str]:

        user_data = repo.find_one_generic("username", data.username)
        ServiceLayerNoneError.when(
            user_data is None, "Incorret username or password"
        )

        hashed_pass = user_data['password']

        ServiceLayerGeneralError.when(
            not await UserAuthentication().verify_password(data.password, hashed_pass), 'Incorrect Username or Password'
        )
 
        data = dict(
            user_id = user_data["_id"],
            username = user_data["username"]
        )

        return {
            "access_token": UserAuthentication().create_access_token(data),
            "refresh_token": UserAuthentication().create_refresh_token(data)
        }

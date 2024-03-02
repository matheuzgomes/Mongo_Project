from ...infra.interface_repositories import IUserRepository
from ..DTOs import ListGenericResponse, LoginUser
from ..DTOs.user import GetUserResponse 
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerPermissionError
from ..service_enums import PermissionEnum

class GetAllUsersService:

    @staticmethod
    def get_all(
        repo:IUserRepository,
        _user_token: LoginUser
        ) -> ListGenericResponse:

        check_permission = repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(PermissionEnum.ADMIN not in check_permission['scopes'], "You don't have the permission to continue with this action.")

        count, data = repo.find_all()
        user_resoonse = [GetUserResponse(
            id = item['_id'],
            username = item['username'],
            name = item['name'],
            description = item['description'] if item.get('description') is not None else None,
            is_active = item['is_active'],
            active_tasks = item['active_tasks'],
            task_limit = item['task_limit']
            ).__dict__ for item in data]

        ServiceLayerNoneError.when(user_resoonse is None, "No data")

        return ListGenericResponse(
            count=count,
            data=user_resoonse
            )

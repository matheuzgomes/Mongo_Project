from ..infra.interface_repositories import IUserRepository
from .DTOs import ListGenericResponse, GetUserResponse
from .service_exceptions import ServiceLayerNoneError

class GetAllUsersService:

    @staticmethod
    def get_all(repo:IUserRepository) -> ListGenericResponse:

        count, data = repo.find_all()
        user_resoonse = [GetUserResponse(
            _id = item['_id'],
            username = item['username'],
            password = item['password'],
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

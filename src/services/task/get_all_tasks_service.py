from ...infra.interface_repositories import ITaskRepository, IUserRepository
from ..DTOs.task import TasksForResponse
from ..DTOs import ListGenericResponse, LoginUser
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerPermissionError
from ..service_enums import PermissionEnum

class GetAllTasksService:

    @staticmethod
    async def get_all(
        repo:ITaskRepository,
        user_repo: IUserRepository,
        _user_token: LoginUser
        ) -> TasksForResponse:

        count, data = await repo.find_all()

        check_permission = user_repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )

        task_response = [TasksForResponse(
            id = item['_id'],
            user_id = item['user_id'],
            task_name= item['task_name'],
            task_status= item['task_status'],
            info = dict(
                description= item['description'] if item.get('description') is not None else None,
                tags= item['tags'] if item.get('tags') is not None else None
            )).__dict__ for item in data]

        ServiceLayerNoneError.when(task_response is None, "No data")

        return ListGenericResponse(
            count=count,
            data=task_response
            )

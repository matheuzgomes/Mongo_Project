from ...infra.interface_repositories import ITaskRepository,IUserRepository
from ..DTOs.task import (GetTaskResponse)
from ..DTOs import LoginUser
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerPermissionError
from ..service_enums import PermissionEnum


class GetTaskService:

    @staticmethod
    async def get(
            repo:ITaskRepository,
            id:int,
            user_repo: IUserRepository,
            _user_token: LoginUser
            ) ->  GetTaskResponse:

        get_task = await repo.find_one(id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not found"
        )

        check_permission = user_repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )

        return GetTaskResponse(
            id = get_task["_id"],
            user_id= get_task["user_id"],
            task_name = get_task["task_name"],
            task_status = get_task["task_status"],
            info= dict(
                description = get_task["description"],
                tags = get_task["tags"]
                )
                ).__dict__

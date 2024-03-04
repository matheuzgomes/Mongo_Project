from ...infra.interface_repositories import ITaskRepository, IUserRepository
from ..DTOs.task import UpdateTaskRequest
from ..DTOs import LoginUser
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerPermissionError
from ..service_enums import PermissionEnum



class UpdateTaskService():

    async def update(
            repo: ITaskRepository,
            data: UpdateTaskRequest,
            task_id: int,
            _user_token: LoginUser,
            user_repo: IUserRepository,
            ) -> None:

        get_task = repo.find_one(task_id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not Found"
        )
        check_permission = user_repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )
        print(data.__dict__)
        update = {"$set" : data.__dict__}
        await repo.update({"_id": task_id}, update)

        return ""

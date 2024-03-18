from datetime import datetime, timezone
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

        user_id = _user_token.user_id

        get_task = await repo.find_one_by_id(task_id=task_id, user_id=user_id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not Found"
        )

        check_permission = user_repo.find_one_by_id(user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )

        update_data = data.__dict__
        update_data["updated_at"] = datetime.now(timezone.utc)

        update = {"$set" : update_data}
        await repo.update({"_id": task_id}, update)

        return ""

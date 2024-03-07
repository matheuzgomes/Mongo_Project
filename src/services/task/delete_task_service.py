from typing import Dict, Any
from ...infra.interface_repositories import ITaskRepository, IUserRepository
from ..DTOs.task import (DeleteDocumentCountResponse)
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerPermissionError
from ..DTOs import LoginUser
from ..service_enums import PermissionEnum


class DeleteTaskService:

    @staticmethod
    async def delete(
            repo:ITaskRepository,
            user_repo: IUserRepository,
            _user_token: LoginUser,
            batch_delete:Dict[str, Any] = None,
            id:int = None
            ) ->  DeleteDocumentCountResponse:

        check_permission = user_repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )

        get_task = await repo.find_one_by_id(task_id=id, user_id=_user_token.user_id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not found"
        )

        if id:
            get_task = await repo.delete(id)
            ServiceLayerNoneError.when(
                get_task == 0, "Task not found"
            )

        elif batch_delete:
            get_task = await repo.delete(batch_delete=batch_delete)
            ServiceLayerNoneError.when(
                get_task == 0, "Task not found"
            )



        return DeleteDocumentCountResponse(count_deleted_tasks=get_task)

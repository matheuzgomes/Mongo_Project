from datetime import datetime, timezone
from ...infra.interface_repositories import ITaskRepository, IUserRepository
from ..DTOs.task import InsertTaskRequest
from ..DTOs import LoginUser
from ..service_exceptions import (
    ServiceLayerNoneError,
    ServiceLayerPermissionError,
    ServiceLayerDuplicateError
)
from ...domain.entities import Task
from ..service_enums import PermissionEnum

class InsertTasksService:

    @staticmethod
    async def insert_tasks(
        repo: ITaskRepository,
        data: InsertTaskRequest,
        _user_token: LoginUser,
        user_repo: IUserRepository,
        ) -> None:

        ServiceLayerNoneError.when(
            data.description is None, "Description field can't be empty"
            )

        ServiceLayerNoneError.when(
            data.task_name is None, "Task name field can't be empty"
            )
        
        find_task = await repo.find_one_by_generic_string_field(
            search_field="task_name",
            value_searched=data.task_name,
            user_id=_user_token.user_id
            )

        ServiceLayerDuplicateError.when(
            find_task is not None, "Task Already Exists"
        )

        check_permission = user_repo.find_one_by_id(_user_token.user_id)
        ServiceLayerPermissionError.when(
            any(element in PermissionEnum.RESPONSABILITY_CHAIN for element in check_permission['scopes']), "You don't have the permission to continue with this action."
            )
        
        data_insert = Task(
            task_name=data.task_name,
            task_status=data.task_status,
            description=data.description,
            is_active=data.is_active,
            user_id=_user_token.user_id,
            tags=data.tags,
            created_at=datetime.now(timezone.utc)
        )

        await repo.insert(data_insert)

        return ""

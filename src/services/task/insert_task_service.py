from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import InsertTaskRequest
from ..DTOs import LoginUser
from ..service_exceptions import ServiceLayerNoneError
from ...domain.entities import Task

class InsertTasksService:

    @staticmethod
    async def insert_tasks(
        db: ITaskRepository,
        data: InsertTaskRequest,
        _user_token: LoginUser
        ) -> None:

        ServiceLayerNoneError.when(
            data.description is None, "Description field can't be empty"
            )
        ServiceLayerNoneError.when(
            data.task_name is None, "Task name field can't be empty"
            )

        data_insert = Task(
            task_name=data.task_name,
            task_status=data.task_status,
            description=data.description,
            is_active=data.is_active,
            user_id=_user_token.user_id,
            tags=data.tags
        )

        await db.insert(data_insert)

        return ""

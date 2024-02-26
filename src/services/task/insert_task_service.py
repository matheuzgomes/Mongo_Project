from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import InsertTaskRequest
from ..service_exceptions import ServiceLayerNoneError
from ...domain.entities import Task

class InsertTasksService:

    @staticmethod
    def insert_tasks(
        db: ITaskRepository,
        data:InsertTaskRequest,
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
            user_id=data.user_id,
            tags=data.tags
        )

        db.insert(data_insert)

        return ""
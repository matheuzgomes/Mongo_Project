from ..infra.interface_repositories import ITaskRepository
from .DTOs import InsertTaskRequest, TasksForResponse
from .service_exceptions import ServiceLayerNoneError
from ..domain.entities import Task

class InsertTasksService:

    @staticmethod
    def insert_tasks(db: ITaskRepository, data:InsertTaskRequest) -> None:

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
            user_id=data.user_id
        )

        db.insert(data_insert)

        return TasksForResponse(
            _id = data_insert._id,
            task_name= data_insert.task_name,
            task_status= data.task_status,
            description= data.description
            )

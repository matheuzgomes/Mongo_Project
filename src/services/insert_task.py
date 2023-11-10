from ..infra.interface_repository import IRepository
from .DTOs import InsertTaskRequest
from .service_exceptions import ServiceLayerNoneError
from ..domain.entities import Task

class InsertTasksService:

    @staticmethod
    def insert_tasks(db: IRepository, data:InsertTaskRequest) -> None:

        ServiceLayerNoneError.when(
            data.description is None, "Description field can't be empty"
            )
        ServiceLayerNoneError.when(
            data.task_name is None, "Task name field can't be empty"
            )

        data_insert = Task(task_name=data.task_name,
                           task_status=data.task_status,
                           description=data.description
        )

        db.insert(data_insert)

        return "Task succesfuly inserted"

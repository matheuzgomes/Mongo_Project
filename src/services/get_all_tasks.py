from ..infra.interface_repositories import ITaskRepository
from .DTOs import TasksForResponse, ListTaskResponse
from .service_exceptions import ServiceLayerNoneError

class GetAllTasksService:

    @staticmethod
    def get_all(repo:ITaskRepository) -> TasksForResponse:

        count, data = repo.find_all()
        task_response = [TasksForResponse(
            _id = item['_id'],
            task_name= item['task_name'],
            task_status= item['task_status'],
            description= item['description'] if item.get('description') is not None else None
            ).__dict__ for item in data]

        ServiceLayerNoneError.when(len(task_response) == 0, "No data")

        return ListTaskResponse(
            count=count,
            data=task_response
            )

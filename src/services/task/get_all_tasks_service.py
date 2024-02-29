from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import TasksForResponse
from ..DTOs import ListGenericResponse
from ..service_exceptions import ServiceLayerNoneError

class GetAllTasksService:

    @staticmethod
    async def get_all(repo:ITaskRepository) -> TasksForResponse:

        count, data = await repo.find_all()
        task_response = [TasksForResponse(
            id = item['_id'],
            user_id = item['user_id'],
            task_name= item['task_name'],
            task_status= item['task_status'],
            info = dict(
                description= item['description'] if item.get('description') is not None else None,
                tags= item['tags'] if item.get('tags') is not None else None
            )).__dict__ for item in data]

        ServiceLayerNoneError.when(task_response is None, "No data")

        return ListGenericResponse(
            count=count,
            data=task_response
            )

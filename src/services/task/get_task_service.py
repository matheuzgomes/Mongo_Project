from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import (GetTaskResponse)
from ..service_exceptions import ServiceLayerNoneError


class GetTaskService:
    @staticmethod
    def get(
            repo:ITaskRepository,
            id:int
            ) ->  GetTaskResponse:
        
        get_task = repo.find_one(id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not found"
        )

        return GetTaskResponse(
            task_id = get_task["task_id"],
            task_name = get_task["task_name"],
            task_status = get_task["task_status"],
            description = get_task["description"],
            tags = get_task["tags"]
        ).__dict__
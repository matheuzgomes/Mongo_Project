from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import (GetTaskResponse)
from ..service_exceptions import ServiceLayerNoneError


class GetTaskService:

    @staticmethod
    async def get(
            repo:ITaskRepository,
            id:int
            ) ->  GetTaskResponse:
        
        get_task = await repo.find_one(id)
        ServiceLayerNoneError.when(
            get_task is None, "Task not found"
        )

        return GetTaskResponse(
            id = get_task["_id"],
            user_id= get_task["user_id"],
            task_name = get_task["task_name"],
            task_status = get_task["task_status"],
            info= dict(
                description = get_task["description"],
                tags = get_task["tags"]
                )
                ).__dict__

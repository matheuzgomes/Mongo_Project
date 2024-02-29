from ...infra.interface_repositories import ITaskRepository
from ..DTOs.task import (GetTaskResponse)
from typing import Dict, Any
from ..service_exceptions import ServiceLayerNoneError
from ..DTOs.task import DeleteDocumentCountResponse


class DeleteTaskService:

    @staticmethod
    async def delete(
            repo:ITaskRepository,
            id:int = None,
            batch_delete:Dict[str, Any] = None
            ) ->  GetTaskResponse:
        
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

        return DeleteDocumentCountResponse(count_delete_tasks=get_task)

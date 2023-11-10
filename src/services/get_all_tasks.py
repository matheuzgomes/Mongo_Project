from ..infra.repository import IRepository
from .DTOs import TasksForResponse

class GetAllTasksService:

    @staticmethod
    def get_all(repo:IRepository) -> TasksForResponse:
        return [TasksForResponse(_id = item['_id'],
                                 task_name= item['task_name'],
                                 task_status= item['task_status'],
                                 description= item['description'] if item.get('description') is not None else None).__dict__ for item in repo.find_all()]

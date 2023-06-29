from typing import Dict
from src.infra.repository import IRepository
from src.domain.entities import Task

class GetAllTasksService:
    
    @staticmethod
    def get(repo:IRepository) -> Dict[Task]:
        return [print(item) for item in repo().find_all()]

from src.services.get_task import GetAllTasksService
from src.infra.repository import MongoRepository



item = GetAllTasksService.get(repo=MongoRepository)

item
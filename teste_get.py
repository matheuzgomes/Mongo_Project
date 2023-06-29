from src.infra.repository import MongoRepository
from dotenv import load_dotenv

load_dotenv()

def find():
    repository = MongoRepository()
    return repository.find_all()


print(find())
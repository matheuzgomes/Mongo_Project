from ...infra.interface_repositories import IUserRepository
from ..DTOs import InsertUserRequest
from ..service_exceptions import ServiceLayerNoneError, ServiceLayerDuplicateError
from ...domain.entities import User
from ...utils import UserAuthentication

class InsertUserService:

    @staticmethod
    def insert_user(db: IUserRepository, data:InsertUserRequest) -> None:

        ServiceLayerDuplicateError.when(
            db.find_one_by_name(field="username", data = data.username) is not None, "User already exists"
        )

        ServiceLayerNoneError.when(
            data.password is None, "Password field can't be empty"
            )
        ServiceLayerNoneError.when(
            data.username is None, "Username field can't be empty"
            )
        hashed_password = UserAuthentication().get_hashed_password(data.password)

        data_insert = User(
            username = data.username,
            password = hashed_password,
            name = data.name,
            description = data.description,
            is_active = True,
            task_limit = 10
        )

        db.insert(data_insert)

        return
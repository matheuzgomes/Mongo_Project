from typing import Any
from datetime import datetime, timezone
from functools import wraps
from ...infra.repositories import LogRepository
from ...domain.entities import Log

def log_factory(db_handler: Any):

    def logging(func):
        repo = LogRepository(db_handler)

        @wraps(func)
        async def wrapper(*args, **kwargs):

            try:

                result = await func(*args, **kwargs)
                await repo.insert(Log(
                    user_id= kwargs['user_token'].user_id,
                    log_date= datetime.now(timezone.utc),
                    function_name= func.__qualname__,
                    is_success= True
                ))

            except Exception as e:

                await repo.insert(
                    Log(
                        user_id= kwargs['user_token'].user_id,
                        log_date= datetime.now(timezone.utc),
                        function_name= func.__qualname__,
                        is_success= False,
                        error_description= {
                            "detail": e.detail,
                            "error_code": e.status_code}
                    ))

                raise e

            return result

        return wrapper

    return logging

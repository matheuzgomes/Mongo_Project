from dataclasses import dataclass
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers import task_route, user_route


@dataclass
class SetupWebapp:

    @staticmethod
    def config_cors(app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"]
        )

    @staticmethod
    def config_routes(app: FastAPI) -> None:
        app.include_router(task_route, prefix="/task", tags=["Task"])
        app.include_router(user_route, prefix="/user", tags=["User"])

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from .webapp_settings import WebappSettings
from .setup_webapp import SetupWebapp

def execute_webapp() -> None:
    load_dotenv()
    webapp_settings = WebappSettings()

    app = FastAPI()

    SetupWebapp.config_cors(app)
    SetupWebapp.config_routes(app)

    @app.get("/healthz", tags=["Health"])
    def health_check():
        return {
            "project_name": webapp_settings.project_name,
            "version": webapp_settings.version,
            "title": webapp_settings.title
        }


    uvicorn.run(app, host=webapp_settings.host)

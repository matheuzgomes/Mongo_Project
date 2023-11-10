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

    uvicorn.run(app, host=webapp_settings.host)

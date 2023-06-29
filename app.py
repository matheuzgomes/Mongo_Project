import uvicorn
from fastapi import FastAPI

def execute_webapp():
    app = FastAPI(title='teste')


    uvicorn.run(app)

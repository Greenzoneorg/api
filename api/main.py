import uvicorn
from fastapi import FastAPI

from . import __env

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.main:app", host=__env.ENVS["HOST"], port=8000, reload=True)
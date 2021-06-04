import logging
import os

import uvicorn
from fastapi import FastAPI

from __env import ENVS
import product_api
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")


app = FastAPI()

os.system("pip install uvicorn")

@app.get("/")
async def root():
    return {"status": ENVS['STATUS']}


@app.get("/products/{id}")
async def product(id: str) -> dict:
    return product_api.get_product(id)
    

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.main:app", host=ENVS["HOST"], port=8000, reload=True)

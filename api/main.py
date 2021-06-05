import logging #import stuff
import os
os.system("pip install -r requirements.txt")
import uvicorn
from fastapi import FastAPI
from rich.logging import RichHandler

from __env import ENVS
import product_api

# set up logging
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")
log.info("Hello, World!")

# initalize the api
app = FastAPI()

# Home route
@app.get("/")
async def root():
    '''Api fuction for the route "/". Returns status.'''
    return {"status": "BUILDING+TESTING"}


# Product Route
@app.get("/products/{id}")
async def product(id: str) -> dict:
    '''Api function for the route "/products/{id}.
        :return: dict.
        :param: id: str    
    '''
    return product_api.get_product(id)


# start the fastapi
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
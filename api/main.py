import logging #import stuff
import os
import uvicorn
from fastapi import FastAPI, Form
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


@app.get("/products")
async def products() -> dict:
    return product_api.get_all()


# Product Route
@app.get("/products/{id}")
async def product(id: str) -> dict:
    '''Api function for the route "/products/{id}.
        :return: dict.
        :param: id: str    
    '''
    return product_api.get_product(id)


@app.post("/addProduct/")
async def add_product(name: str = Form(...), imgLink: str = Form(...),disc: str = Form(...),keyWords: str = Form(...),materials: str = Form(...), isReuse: str = Form(...), isRecycle: str = Form(...), howtoRe: str = Form(...) ):
    add_product(name, imgLink, disc, keyWords, materials, isReuse, isRecycle, howtoRe)
    return "added (hopefully)"
    

# start the fastapi
def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
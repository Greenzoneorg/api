from uuid import uuid4
from deta import Deta

from typing import Union
from __env import ENVS

from fastapi import HTTPException
#connect to db
deta = Deta(ENVS["DETA_KEY"])
db = deta.Base("products")


# productId
# userId
# fields --- name , imgLink :
#  details --- description , keyWords , materials , isReuse , isRecycle , howtoRe
#


def get_all() -> dict:
    return db.fetch(query=None, buffer=None)
    


def get_product(id: str) -> Union[dict, HTTPException]:
    '''
    Get the product from the DB and return it. If the id is invalid, return error.
    :param: id: str
    :return: dict or HTTPException
    '''
    global db #get the db
    try:
        product = next(db.fetch({"productId": id}))[0] # get the product from the db
    except IndexError:
        raise HTTPException(status_code=404, message="Product not found") #if product is not found, return error
    return product

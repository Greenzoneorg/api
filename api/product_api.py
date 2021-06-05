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


def get_product(id: str) -> Union[dict, HTTPException]:
    '''
    Get the product from the DB and return it. If the id is invalid, return error.
    :param: id: str
    :return: dict or HTTPException
    '''
    global db
    try:
        product = next(db.fetch({"productId": id}))[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

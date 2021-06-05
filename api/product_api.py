from uuid import uuid4
from deta import Deta

from typing import Union
from __env import ENVS


deta = Deta(ENVS["DETA_KEY"])
db = deta.Base("products")


# productId
# userId
# fields --- name , imgLink :
#  details --- description , keyWords , materials , isReuse , isRecycle , howtoRe
#


def get_product(id: str) -> Union[dict, str]:
    global db
    try:
        prodcut = next(db.fetch({"productId": id}))[0]
    except IndexError:
        return "Product Not Found"
    return prodcut

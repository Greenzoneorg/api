from deta import Deta

from __env import ENVS

#! FILE TO TEST ADDING STUFF TO THE DB



deta = Deta(ENVS["DETA_KEY"])
db = deta.Base("products")

db.insert(
    {
        "productId": "milkPaper1",
        "userId": "00001",
        "fields": {
            "name": "Product!",
            "imgLink": "https://www.bra.org/wp-content/uploads/guide-paper-cartonmilk.jpg",
            "details": {
                "description": "Milk carton made of paper",
                "keyWords": "milk, carton, paper",
                "materials": "paper, plastic",
                "isReuse": "True",
                "isRecycle": "True",
                "howtoRe": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
            },
        },
    }
)

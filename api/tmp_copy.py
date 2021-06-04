from deta import Deta

from __env import ENVS


deta = Deta(ENVS['DETA_KEY'])
db = deta.Base('product')

db.insert({
    "productId": "milkPaper1",
    "userid": "00001",
    "fields":{
        "name":"",
        "imgLink":"https://www.bra.org/wp-content/uploads/guide-paper-cartonmilk.jpg",
        "details": {
            "description":"Milk carton made of paper",            
            "keyWords":"milk, carton, paper",
            "materials":"paper, plastic",
            "isReuse": "True",
            "isRecycle": "True",
            "howtoRe":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco"
        }
    },
    
})
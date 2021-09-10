
from requests import post, get


class SealDocument:
    def __init__(self):
        return

    def seal(self, token, doc):
        
        header = {"Authorization": "Bearer" + token,'Content-type': 'application/json'}
        response = post("https://api.scribital.com/v1/seal", json=doc, headers=header)
        return response.content


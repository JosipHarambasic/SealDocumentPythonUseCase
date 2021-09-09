import requests


class UserCredentials:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def createToken(self):
        data = {'username': self.username, 'api-key': self.api_key}
        response = requests.post('https://api.scribital.com/v1/access/login', json=data)
        return response.content.decode("utf-8")



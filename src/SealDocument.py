
from requests import post, get


class SealDocument:
    def __init__(self):
        return

    def seal(self, token, content):

        data = {"content": content,
                "account_name":"ais_demo_seal",
                "visual_signature":{
                    "position":{
                        "x":20,
                        "y":20,
                        "width":100,
                        "height":100,
                        "page":"0"
                    }
                }}
        header = {"Authorization": "Bearer" + token}
        response = post("https://api.scribital.com/v1/seal", json=data, headers=header)
        print(data)
        return response.content

        """header = {"Authorization": "Bearer" + token}
        response = get("https://api.scribital.com/v1/seal", json=documentAsJSON, headers=header)
        return response.content"""
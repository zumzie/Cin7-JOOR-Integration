import requests
import json
import grab_token
import pandas

class cin7API:
    def __init__(self):
        self.base_url = "https://api.cin7.com/api"
        self.username = "JOORAU"
        self.access_token = grab_token.cinKEY
        self.session = requests.Session()
        self.session.auth = (self.username, self.access_token)
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def paginate(self, endpoint, params=None):
        results = []
        while endpoint:
            response = self.session.get(endpoint, params=params)
            data = response.json()
            results.extend(data["data"])
            endpoint = data["links"].get("next")
        return results






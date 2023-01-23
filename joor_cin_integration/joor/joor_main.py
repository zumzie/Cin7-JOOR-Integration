import requests
import grab_token as gb

class joorAPI:
    API_TOKEN = gb.joor_token
    def __init__(self):
        self.header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_TOKEN}"
        }
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })


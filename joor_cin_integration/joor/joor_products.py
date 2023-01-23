import sys
sys.path.append('/config')
sys.path.append('./joor_cin_integration/cin7')
sys.path.append('/joor_cin_integration/utils')

from cin_products import cin7Products
import asyncio
import requests

import json
import grab_token as gb
from requests import sessions


class joorstyles():
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
        self.bulk_list = []
    
    # Styles

    def get_styles():
        pass

    def create_styles():
        pass

    def update_styles():
        pass

    def create_bulkstyles(self):
        pass

    def delete_styles():
        pass



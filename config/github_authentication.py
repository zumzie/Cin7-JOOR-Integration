import sys
sys.path.append('G:/DEVL/django_integration/joor_cin_integration/utils')
import grab_token
import json
import requests


class GitHubAuth:
    username = "christianagu"
    access_token = grab_token.gitKEY
    settings = "BrandSettings"
    config_path = "Configs/Sandbox/"
    def __init__(self):
        self.authorization = f"{self.username}:{self.access_token}" 
        
    def create_session(self):    
        session = requests.Session()
        session.headers.update({
            "Content-Type": "application/json"
        })       
        session.headers.update({
            "Authorization": f"Bearer {self.authorization}",
        })
        return session     
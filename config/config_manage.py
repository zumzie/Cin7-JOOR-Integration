import sys
sys.path.append('/config')
sys.path.append('/joor_cin_integration/joor')
sys.path.append('/joor_cin_integration/utils')
import json
import grab_token
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



class Config:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.auth = GitHubAuth()
        self.session = self.auth.create_session()
        self.session.headers.update({
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        })

    def get_store_config(self):
        self.auth = GitHubAuth()
        self.repo_url = f'{self.base_url}/{self.auth.username}/{self.auth.settings}/contents/{self.auth.config_path}'
        response = self.session.get(self.repo_url)
        return response.json()
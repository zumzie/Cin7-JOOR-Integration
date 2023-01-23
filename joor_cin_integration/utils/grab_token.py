import os
from pathlib import Path
from dotenv import load_dotenv
import base64

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
joor_token = os.environ['joorKEY']

# Basic Auth
cinKEY = os.environ['cinKEY']


#Oauth2
"""
joorKEY = os.environ['joorKEY']
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
USERNAME = os.environ['USERNAME']
PASSW = os.environ['PASSW']
account_id = os.environ['account_id']
user_id = os.environ['user_id']


"""
joor_token = base64.b64encode(joor_token.encode('ascii')).decode('utf8')

def get_github_token():
    # Github
    gitKEY = os.environ['github_token']
    #gitKEY = base64.b64encode(gitKEY.encode('ascii')).decode('utf8')
    return gitKEY

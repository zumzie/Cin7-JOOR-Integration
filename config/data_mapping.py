import os
import json
from github import Github
import time
import sys
sys.path.append('./joor_cin_integration/utils')
import grab_token as gb


class DataMapper:
    def __init__(self):
        self.repo_name = "BrandSettings" # Name of repository
        self.repo_owner = "zumzie" # username
        self.config_folder = "Configs/Sandbox" # folder path
        self.access_token = gb.get_github_token() # access token for github
        self.g = Github(self.access_token) # creates a github object using the access token

    def map_data(self):
        repo = self.g.get_repo(f"{self.repo_owner}/{self.repo_name}") # get the repo object
        config_settings = {} # empty dictionary to store the config settings
        try:
            config_files = repo.get_contents(self.config_folder) # get the contents of the config folder
            for config_file in config_files:
                config_settings[config_file.name] = json.loads(config_file.decoded_content) # store the config settings in the dictionary
        except Exception as e:
            print(e) # Print the error if so
            return None

        return config_settings['default_config.json']

    def map_data_container(self, data_container_file):
        # Retrieve the data container file from the GitHub repository
        data_container = self.g.get_contents(self.config_folder + '/' + data_container_file)
        # Parse the data container file into a dictionary
        data_container_dict = json.loads(data_container.decoded_content)
        # Use the keys of the dictionary to map the values to the payload
        payload = {}
        for key in data_container_dict:
            payload[key] = data_container_dict[key]
        for key in self.config_settings:
            payload_key = self.config_settings[key]
            payload = eval(payload_key)
        return payload


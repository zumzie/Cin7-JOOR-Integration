import sys
sys.path.append('/config')
sys.path.append('./joor_cin_integration/cin7')
sys.path.append('/joor_cin_integration/utils')

from cin_products import cin7Products
import asyncio
import requests
from data_mapping import DataMapper
import ast

import json
import grab_token as gb
from requests import sessions


class joor_bulk():
    API_TOKEN = gb.joor_token
    my_products = cin7Products()
    git_config = DataMapper()
    my_products = cin7Products()
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
        self.mapped_variables = {}
        self.style_dict = {}
        self.temp_list = []
        self.config_settings = self.git_config.map_data()
        
    
    # Styles
    def map_curproduct(self):
        # Retrieve the data container file from the GitHub repository
        # Parse the data container file into a dictionary
        # Use the keys of the dictionary to map the values to the payload
        organized_prods = self.my_products.organize_products()
        for product in organized_prods:
            cur_product = product
            self.mapped_variables["cur_product"] = cur_product
        return self.mapped_variables

    def format_bulk_data(self, cur_products):
        bulk_style_list = []
        self.cur_product = cur_products
        print(cur_products)
        print((self.config_settings['flows_settings']['styles']["eval_style_number"]))
        print(eval(self.config_settings['flows_settings']['styles']["eval_style_name"]))
            


        for fields in self.cur_product:
            self.style_dict = {
                "style_number": eval(self.config_settings['flows_settings']['styles']['eval_style_number']),
                "style_name": eval(self.config_settings['flows_settings']['styles']["eval_style_name"]),
                "style_code": eval(self.config_settings['flows_settings']['styles']["eval_style_code"]),
                "style_description": eval(self.config_settings['flows_settings']['styles']["eval_style_description"]),
                "style_color": eval(self.config_settings['flows_settings']['styles']["eval_style_color"]),
                "style_size": eval(self.config_settings['flows_settings']['styles']["eval_style_size"])
            }
            print(fields,'\n')

            bulk_style = {"bulk_style": {"style": self.style_dict}}
        return bulk_style



 
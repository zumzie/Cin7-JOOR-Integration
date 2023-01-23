import requests
import json
import asyncio
from cin7_main import cin7API
import sys
sys.path.append('/joor_cin_integration/utils')
import grab_token

class cin7Products(cin7API):
    def __init__(self):
        cin7API.__init__(self)
        self.all_products = []
    # Retreives a list of products
    def get_products(self, page, rows):
        url = f"{self.base_url}/v1/Products"
        params = {
            'page': page,
            'rows': rows,
        }

        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Grabs a list of the products
    def list_of_products(self):
        page = 1
        rows = 250
        while True:
            products = self.get_products(page, rows)
            if not products:
                break
            self.all_products.extend(products)
            page +=1
        return self.all_products

    # either have this function grab the style data that can be sent to joor
    # and organize it, or just use list function for the joor_wrapper.py bulkstyle_create function
    def organize_products(self):
        organized_prods = self.list_of_products()
        new_list = []
        
        for products in organized_prods:
            new_list.append(products)
        return new_list


my_products = cin7Products()



""""
Build on this code below to use the config to modify


with open('config.json') as json_file:
    config = json.load(json_file)

name = config["option_settings"]["size"]
product_type = payload["styles"]["eval_silhouette"]
payload["options_settings"]["size"] = f"{size_name} - {product_type}"

my_products.organize_products()["options_settings"]["size"] = f"{size_name} - {product_type}"

"""
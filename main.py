import sys
sys.path.append('./config')
sys.path.append('./joor_cin_integration/joor')
sys.path.append('./joor_cin_integration/utils')
sys.path.append('./joor_cin_integration/data_modifier')
import data_mapping as dm
import json
import data_transformers as transformer

git_config = dm.DataMapper()
cur_prod  = transformer.joor_bulk()
cur_prod_var = cur_prod.map_curproduct()
bulk_style = cur_prod.format_bulk_data(cur_prod_var)

print(bulk_style)

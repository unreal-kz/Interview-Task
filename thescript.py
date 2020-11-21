# Python script file
import os
import pathlib

import json, jsonschema

from schema import Schema
from jsonschema import validate



json_data, schema_list = [], []
schema_dict = {}

json_folder = pathlib.Path.cwd() / 'event'
schema_folder = pathlib.Path.cwd() / 'schema'

# Testing
# for k,v in enumerate(sorted(os.listdir(json_folder))) :
#     print(k, v)

# Reading 16 json files from 'event' folder
for file in sorted(os.listdir(json_folder)):
    with open(os.path.join(json_folder, file) , 'r') as f:
        json_data.append(json.load(f))
        
# Testing
# print(len(result))
# for k,v in enumerate(json_data):
#     if isinstance(v,dict) and 'event' in v:
#         print(k, v['event'])
#     else:
#         print(k, 'Not')

# Reading .schema files from 'schema' folder
# print (os.listdir(schema_folder))
for k,v in enumerate(os.listdir(schema_folder)):
    key = v.split('.')[0]
    with open(os.path.join(schema_folder, v)) as f:
        schema_dict[key] = f.read()
        # schema_dict[key] = json.loads(f.read())
        # Testing
        # schema_list.append(f.read())

# Testing
# print (schema_dict)
# res = json.loads(schema_list[0])
# print (type(res))
# print (res.keys())

# print(res['type'])
# print(res['$schema'])
# print(res['required'])
# print('-----------')
# print(res['properties'])

#Testing
# print(schema_dict.keys())
# print(schema_dict['label_selected'])
# for k,v in schema_dict:
#     print(schema_dict.keys())
#     print(schema_dict[k].keys())
#     print('------------------------------------------------------------')

# Function for validation of json files against 4 available schemas
def validateJson(jsonData, schemaData):
    try:
        validate(instance=jsonData, schema=schemaData)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Cheking for validity
for jdata in json_data:
    if isinstance(jdata,dict) and 'event' in jdata:
        print(jdata['event'])
        # for k,v in schema_dict.items():
        if jdata['event'] in schema_dict: 
            is_valid = validateJson(jdata, schema_dict[jdata['event']])
            event = jdata['event']
            print (f'{event} evnt is json file?: {is_valid}')
import os
import yaml
import json
import configparser

if os.path.isfile('config.json'):
    os.remove('config.json')

if os.path.isfile('config.yaml'):
    os.remove('config.yaml')

if os.path.isfile('config.ini2'):
    os.remove('config.ini2')

config = configparser.ConfigParser()
config.read('config.ini')

print(dict(config.items()))

dict = {'kevin': {'int': 3, 'string':'string'}}
config.read_dict(dict)

with open('config.ini2', 'w') as f:
    config.write(f)

config_dict = config._sections # Create a dict

# JSON
with open('config.json', 'w') as f:
    json.dump(config_dict, fp=f, indent=2)

with open('config.json') as f:
    json_config = json.load(f)
    print(json_config)

# YAML
with open('config.yaml', 'w') as f:
    yaml.dump(config_dict, stream=f, indent=2)

with open('config.yaml') as f:
    yaml_config = yaml.load(f, Loader=yaml.FullLoader)
    print(yaml_config)
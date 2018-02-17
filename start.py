import os, utils

#Calling menu
utils.menu()


import json, pprint, toml, os
conf_file = "config.toml"
if os.path.exists(conf_file):
    with open(conf_file, encoding='utf-8') as f:
        try:
            conf = toml.loads(f.read())
        except:
            print("Could not read file:", conf_file)
            
pprint.pprint(conf)

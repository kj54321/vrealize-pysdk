#!/usr/bin/env python3
import os, vralib, json

# set proxy
proxy='socks5://127.0.0.1:1090'
os.environ['HTTP_PROXY'] = proxy
os.environ['HTTPS_PROXY'] = proxy

# vra login
vra = vralib.Session.login('i343176@ycs.io', 
                            'Hybris_sap@12345!', 
                            '10.248.34.44', 
                            'YCOMMERCE', 
                            ssl_verify=False)

resource_id = '731d6caf-99c3-4866-99e6-23ff22bf78d5'
action_id = 'cb85d16f-4ced-44b2-9c04-8247c802fe65'

# get template
d = vra.get_resource_action_template(resource_id,action_id)
# Insert value to dict
d['description'] = 'API execution test!'
d['data']['ForceDestroy'] = 'true'
d = vra.request_resource_action(resource_id,action_id)
# convert dict to json
payload = json.dumps(d)
# call post func
build = vra.request_resource_action(resource_id,action_id, payload)
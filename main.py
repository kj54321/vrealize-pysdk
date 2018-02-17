#!/usr/bin/env python3
# Check if dc exists
try:
    from utils import check_dc
except ImportError:
    pass
check_dc()

import os, time ,re
from utils import _conf, clear_scr, dc

##################
# Load basic conf if exists
c=_conf()
# Populate config if not None
for i in ['username', 'password', 'tenant']:
    j = c['default'].get(i)
    # Check if i exists
    if j is None or '':
        print("Missing value for " + i + "!")
        j = input("Please input " + "\033[1m" + i + "\033[0m:\n")
    else:
        pass
    # Assign value
    exec(i + '=j')

# Assign value per dc specific
for i in ['cloudurl',
          'createEdge',
          'createVM',
          'createNFS',
          'createIPA',
          'createCMZ',
          'createVIP',
          'createHDBS',
          'createHDBC',
          'removeNFS',
          'removeIPA',
          'removeVIP']:
    j = c[dc].get(i)
    exec(i + '=j')

# Initialize Session
import vralib, json
proxy='socks5://127.0.0.1:1090'
os.environ['HTTP_PROXY'] = proxy
os.environ['HTTPS_PROXY'] = proxy
vra = vralib.Session.login(username, 
                           password, 
                           cloudurl, 
                           tenant, 
                           ssl_verify=False)
d = vra.get_request_template(createHDBC)
###################
# Get Project Info

def get_cid():
    cid = input("""
Please input 3 lower letter Customer Short Code(cid)
example: bse, tcl, ccc
""")
    if re.match("^[a-z]{3}$",cid):
        print("Validation OK!")
        return cid
    else:
        return get_cid()

def get_pid():
    pid = input("Please input Project ID(\033[1mb2b/b2c\033[0m): \n")
    if re.match("^(b2b|b2c)$",pid):
        print("Validation OK!")
        return pid
    else:
        return get_pid()

def get_env():
    env =  input("""
Please input type of env:
example: d1, s2, p3
""")
    if re.match("^[a-z]{1}[1-9]{1}$",env):
        print("Validation OK!")
        return env
    else:
        return get_env()


print(c)
print(dc)
print()
print()
print(d)

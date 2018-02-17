import re
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
    pid = input("Please input project id(\033[1mb2b/b2c\033[0m): \n")
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

a = get_cid()
b = get_pid()
c = get_env()
print(a)
print(b)
print(c)

#!/usr/bin/env python3
import os, time, toml
#from pathlib import Path
#dict_ip = {'ro1':'1.1.1.1', 'sy2':'2.2.2.2', 'mo2': '3.3.3.3', 'sh3':'4.4.4.4'}
#for key,val in dict_ip.items():
#    exec(key + '=val')
def _conf():
    conf_file = "config.toml"
    if os.path.exists(conf_file):
        with open(conf_file, encoding='utf-8') as f:
            try:
                c = toml.loads(f.read())
            except:
                print("Could not read file:", conf_file)
    return c

def clear_scr():
    def cls():
        print(('\n'*80))    # pseudo clearance on Win
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    
    clear_scr()
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("""
              1. Datacenter
              2. Deploy new enviroment
              3. Deploy configuration on F5
              4. Search vm's in vmware
              5. Snapshots vm's in vmware
              6. Create DNS entries
              0. Exit
            """)
    print (30 * '-')
#    if dc_ip != None:
    if 'dc' in globals():
        print (30 * '-')
        print (" YOUR SETTINGS")
        print (30 * '-')
        print ("DC: "+ dc + " - "+ _conf()[dc]['cloudurl'])
#    if memory.last_status != None:
#        print (30 * '-')
#        print (" Last build status: completed")
#        print (30 * '-')
          
    ## Get input ###
    choice = input('Enter your choice [1-0] : ')
     
    ### Convert string to int type ##
    choice = int(choice)
     
    ### Take action as per selected menu-option ###
    if choice == 1:
        global_dc()
    elif choice == 2:
        import main
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 0:
            print ("Bye bye...")
            time.sleep(3)
            os._exit(0)

    else:    ## default ##
            print ("Invalid number. Try again...")

def global_dc():
    global dc
    clear_scr()
    print (30 * '-')
    print (" Choose DC for VRA")
    print (30 * '-')
    print ("""
              1. ROT - 1.2
              2. SYD - 1.2
              3. MOS - 1.2
              4. NSQ - 1.2
              5. SHA - 1.2
              6. ROT - Easy
              7. SYD - Easy
            """)
    print (30 * '-') 
    ## Get input ###
    choice = input('Enter your choice [1-6] : ')
     
    ### Convert string to int type ##
    try:
        choice = int(choice)
    except:
        pass
     
    ### Take action as per selected menu-option ###
    if choice == 1:
            dc = 'ro1'
            menu()
    elif choice == 2:
            dc = 'sy2'
            menu()
    elif choice == 3:
            dc = 'mo2'
            menu()
    elif choice == 4:
            dc = 'ns3'
            menu()
    elif choice == 5:
            dc = 'sh3'
            menu()
    elif choice == 6:
            dc = 'ro1-easy'
            menu()   
    else:    ## default ##
            print ("ups...")
            global_dc()            
    return dc

def check_dc():
#    if dc == None:
    if 'dc' in globals():
        return dc
    else:
        print(20 * "#" + " Please choose DC first " + 20 * "#")
        time.sleep(3)
        return global_dc()
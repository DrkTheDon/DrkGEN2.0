#!/usr/bin/python3
# pylint: disable=E1101

#####################################################
## DrK Generator 2.0 (DrkGen)                      ##
## A AOI Giftcard Generator and Checker            ##
## https://drkbro.dev/drk-softwares                ##
## Coded by: drk                                   ##
#####################################################

# Imports IGNORE UNNESCESARY IMPORTS THEY ARE FROM OTHER PROJECTS
from logging import exception
from urllib.parse import uses_fragment
import discord
from pystyle import Colorate, Colors # NEW LIB
import time
import os
from datetime import datetime
import requests
import numpy
import random
import requests
import re
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
import os
import json as jsond  # json
import time  # sleep before exit
import binascii  # hex encoding
from uuid import uuid4  # gen random guid
import platform  # check platform
import subprocess  # needed for mac device
import hmac # signature checksum
import hashlib # signature checksum
from pypresence import Presence
import pypresence

# Global Variables
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "Nuhish#4697"
client_id = "1194593398804451440"

RPC = Presence(client_id)
invalid = 0
valid = 0


import os
import json as jsond  # json
import time  # sleep before exit
import binascii  # hex encoding
from uuid import uuid4  # gen random guid
import platform  # check platform
import subprocess  # needed for mac device
import hmac # signature checksum
import hashlib # signature checksum

try:
    if os.name == 'nt':
        import win32security  # get sid (WIN only)
    import requests  # https requests
except ModuleNotFoundError:
    print("Exception when importing modules")
    print("Installing necessary modules....")
    if os.path.isfile("requirements.txt"):
        os.system("pip3 install -r requirements.txt")
    else:
        if os.name == 'nt':
            os.system("pip3 install pywin32")
        os.system("pip3 install requests")
    print("Modules installed!")
    time.sleep(1.5)
    os._exit(1)

class api:
    name = ownerid = secret = version = hash_to_check = ""

    def __init__(self, name, ownerid, secret, version, hash_to_check):
        if len(ownerid) != 10 and len(secret) != 64:
            print("Go to Manage Applications on dashboard, copy python code, and replace code in main.py with that")
            time.sleep(3)
            os._exit(1)
    
        self.name = name

        self.ownerid = ownerid

        self.secret = secret

        self.version = version
        self.hash_to_check = hash_to_check
        self.init()

    sessionid = enckey = ""
    initialized = False

    def init(self):
        if self.sessionid != "":
            print("You've already initialized!")
            time.sleep(3)
            os._exit(1)

        sent_key = str(uuid4())[:16]
        
        self.enckey = sent_key + "-" + self.secret
        
        post_data = {
            "type": "init",
            "ver": self.version,
            "hash": self.hash_to_check,
            "enckey": sent_key,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        if response == "KeyAuth_Invalid":
            print("The application doesn't exist")
            time.sleep(3)
            os._exit(1)

        json = jsond.loads(response)

        if json["message"] == "invalidver":
            if json["download"] != "":
                print("New Version Available")
                download_link = json["download"]
                os.system(f"start {download_link}")
                time.sleep(3)
                os._exit(1)
            else:
                print("Invalid Version, Contact owner to add download link to latest app version")
                time.sleep(3)
                os._exit(1)

        if not json["success"]:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

        self.sessionid = json["sessionid"]
        self.initialized = True
        
        if json["newSession"]:
            time.sleep(0.1)

    def register(self, user, password, license, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "register",
            "username": user,
            "pass": password,
            "key": license,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print(json["message"])
            self.__load_user_data(json["info"])
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def upgrade(self, user, license):
        self.checkinit()

        post_data = {
            "type": "upgrade",
            "username": user,
            "key": license,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print(json["message"])
            print("Please restart program and login")
            time.sleep(3)
            os._exit(1)
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def login(self, user, password, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "login",
            "username": user,
            "pass": password,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
            print(json["message"])
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def license(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "license",
            "key": key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
            print(json["message"])
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def var(self, name):
        self.checkinit()

        post_data = {
            "type": "var",
            "varid": name,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def getvar(self, var_name):
        self.checkinit()

        post_data = {
            "type": "getvar",
            "var": var_name,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["response"]
        else:
            print(f"NOTE: This is commonly misunderstood. This is for user variables, not the normal variables.\nUse keyauthapp.var(\"{var_name}\") for normal variables");
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def setvar(self, var_name, var_data):
        self.checkinit()

        post_data = {
            "type": "setvar",
            "var": var_name,
            "data": var_data,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def ban(self):
        self.checkinit()

        post_data = {
            "type": "ban",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def file(self, fileid):
        self.checkinit()

        post_data = {
            "type": "file",
            "fileid": fileid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if not json["success"]:
            print(json["message"])
            time.sleep(3)
            os._exit(1)
        return binascii.unhexlify(json["contents"])

    def webhook(self, webid, param, body = "", conttype = ""):
        self.checkinit()

        post_data = {
            "type": "webhook",
            "webid": webid,
            "params": param,
            "body": body,
            "conttype": conttype,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def check(self):
        self.checkinit()

        post_data = {
            "type": "check",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)
        if json["success"]:
            return True
        else:
            return False

    def checkblacklist(self):
        self.checkinit()
        hwid = others.get_hwid()

        post_data = {
            "type": "checkblacklist",
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)
        if json["success"]:
            return True
        else:
            return False

    def log(self, message):
        self.checkinit()

        post_data = {
            "type": "log",
            "pcuser": os.getenv('username'),
            "message": message,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        self.__do_request(post_data)

    def fetchOnline(self):
        self.checkinit()

        post_data = {
            "type": "fetchOnline",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            if len(json["users"]) == 0:
                return None
            else:
                return json["users"]
        else:
            return None
            
    def fetchStats(self):
        self.checkinit()

        post_data = {
            "type": "fetchStats",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_app_data(json["appinfo"])
            
    def chatGet(self, channel):
        self.checkinit()

        post_data = {
            "type": "chatget",
            "channel": channel,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["messages"]
        else:
            return None

    def chatSend(self, message, channel):
        self.checkinit()

        post_data = {
            "type": "chatsend",
            "message": message,
            "channel": channel,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            return False

    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            time.sleep(3)
            os._exit(1)

    def changeUsername(self, username):
        self.checkinit()

        post_data = {
            "type": "changeUsername",
            "newUsername": username,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print("Successfully changed username")
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)  

    def logout(self):
        self.checkinit()

        post_data = {
            "type": "logout",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print("Successfully logged out")
            time.sleep(3)
            os._exit(1)
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)         
            
    def __do_request(self, post_data):
        try:
            response = requests.post(
                "https://keyauth.win/api/1.2/", data=post_data, timeout=10
            )
            
            key = self.secret if post_data["type"] == "init" else self.enckey
            if post_data["type"] == "log": return response.text
                        
            client_computed = hmac.new(key.encode('utf-8'), response.text.encode('utf-8'), hashlib.sha256).hexdigest()
            
            signature = response.headers["signature"]
            
            if not hmac.compare_digest(client_computed, signature):
                print("Signature checksum failed. Request was tampered with or session ended most likely.")
                print("Response: " + response.text)
                time.sleep(3)
                os._exit(1) 
            
            return response.text
        except requests.exceptions.Timeout:
            print("Request timed out. Server is probably down/slow at the moment")

    class application_data_class:
        numUsers = numKeys = app_ver = customer_panel = onlineUsers = ""

    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = subscriptions = ""

    user_data = user_data_class()
    app_data = application_data_class()

    def __load_app_data(self, data):
        self.app_data.numUsers = data["numUsers"]
        self.app_data.numKeys = data["numKeys"]
        self.app_data.app_ver = data["version"]
        self.app_data.customer_panel = data["customerPanelLink"]
        self.app_data.onlineUsers = data["numOnlineUsers"]

    def __load_user_data(self, data):
        self.user_data.username = data["username"]
        self.user_data.ip = data["ip"]
        self.user_data.hwid = data["hwid"] or "N/A"
        self.user_data.expires = data["subscriptions"][0]["expiry"]
        self.user_data.createdate = data["createdate"]
        self.user_data.lastlogin = data["lastlogin"]
        self.user_data.subscription = data["subscriptions"][0]["subscription"]
        self.user_data.subscriptions = data["subscriptions"]


class others:
    @staticmethod
    def get_hwid():
        if platform.system() == "Linux":
            with open("/etc/machine-id") as f:
                hwid = f.read()
                return hwid
        elif platform.system() == 'Windows':
            winuser = os.getlogin()
            sid = win32security.LookupAccountName(None, winuser)[0]  # You can also use WMIC (better than SID, some users had problems with WMIC)
            hwid = win32security.ConvertSidToStringSid(sid)
            return hwid
            '''
            cmd = subprocess.Popen(
                "wmic useraccount where name='%username%' get sid",
                stdout=subprocess.pip3E,
                shell=True,
            )

            (suppost_sid, error) = cmd.communicate()

            suppost_sid = suppost_sid.split(b"\n")[1].strip()

            return suppost_sid.decode()

            ^^ HOW TO DO IT USING WMIC
            '''
        elif platform.system() == 'Darwin':
            output = subprocess.Popen("ioreg -l | grep IOPlatformSerialNumber", stdout=subprocess.PIPE, shell=True).communicate()[0]
            serial = output.decode().split('=', 1)[1].replace(' ', '')
            hwid = serial[1:-2]
            return hwid

# Global Variables 2nd Time
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "Nuhish#4697"
client_id = "1194593398804451440"

RPC = Presence(client_id)
invalid = 0
valid = 0


# KEY AUTH
def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "DrkGEN 2.0",
    ownerid = "W1eEwQCCGT",
    secret = "6571944b4695f42f358777468b0e6355561725ca5f88937f695561374359a6fa",
    version = "1.0",
    hash_to_check = getchecksum()
)
RPC_CHECK = ""

def keyauthtry():
    try:
        with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
            answer = DISCORD_RPC_FILE.read()
            if answer == "NO":
                pass
            elif answer == "YES":
                RPC.connect()

                RPC.update(
                    state="In Login Page - V. 0.857 BETA",
                    large_image="icon",
                    buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
        )
            else:
                print("Discord error noticed, contact drk in a support ticket.")
                time.sleep(5)
                quit()
        print(Colorate.Horizontal(Colors.green_to_red, """
V. 0.857 CLOSED BETA                   discord.gg/9y9HCzawBe            
  _      ____   _____ _____ _   _   _____        _____ ______ 
 | |    / __ \ / ____|_   _| \ | | |  __ \ /\   / ____|  ____|
 | |   | |  | | |  __  | | |  \| | | |__) /  \ | |  __| |__   
 | |   | |  | | | |_ | | | | . ` | |  ___/ /\ \| | |_ |  __|  
 | |___| |__| | |__| |_| |_| |\  | | |  / ____ \ |__| | |____ 
 |______\____/ \_____|_____|_| \_| |_| /_/    \_\_____|______|
                                                              
                                                                            """))
        print(f'''{Colors.white}                {Colors.blue}    [ LOGIN PAGE ]{Colors.white}''')
        print("""\n\n
[1] Login
[2] Register [License key required]
              
[3] Troubleshooting [Discord Errors etc]
              
[4] Upgrade   
[5] Quit
              
        """)
        ans = input("Select Option: ")
        if ans == "1":
            user = input('Provide username: ')
            password = input('Provide password: ')
            keyauthapp.login(user, password)     
        elif ans == "2":
            user = input('Provide username: ')
            password = input('Provide password: ')
            license = input('Provide License: ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            clearcmd()
            print("""
Do you have discord installed on this machine?
                
[1] Yes
[2] No

[3] Back""")
            dcans = input(f"\nOption\n{Colors.red}>{Colors.white}")

            if dcans == "1":
                clearcmd()
                print("Open a new support ticket and send all the reuqired details!\n")
                back()
                clearcmd()
                keyauthtry()
            elif dcans == "2":
                with open("./assets/discordrpc.txt", "w+") as file:
                        file.write("NO")
                        file.close()
                clearcmd()
                time.sleep(0.3)
                print(f"{Colors.green}[+]{Colors.white} Sucessfully Turned of Discord Rich Presence.{Colors.white}")
                time.sleep(0.5)
                back()
                clearcmd()
                keyauthtry()
            elif dcans == "3":
                clearcmd()
                keyauthtry()
        elif ans == "4":
            user = input('Provide username: ')
            license = input('Provide License: ')
            keyauthapp.upgrade(user, license)
        elif ans == "5":
            clearcmd()
            quit()
        else:
            print("\nInvalid option")
            sleep(1)
            clearcmd()
            keyauthtry()
    except KeyboardInterrupt:
        clearcmd()
        keyauthtry()
# Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def back():
    input(f"{Colors.blue}Press enter to continue.")
def underdev():
    print(f"{Colors.red}{curtime}{Colors.white} This is currently under development.")
    back()
    clearcmd()
def settings():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="In Settings - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
    ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
    ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
    ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
    ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
    ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝                                                                                                                                                                                                                                              
    """))
    print(f"""      Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"""
    [1] UI Settings [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [2] License key [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [3] Clear Cache [{Colors.green}STABLE{Colors.white}]
    [4] Skip Intro [{Colors.green}STABLE{Colors.white}]
    [5] Sleep Check [{Colors.green}STABLE{Colors.white}]
    [6] Discord Rich Presence Settings [{Colors.green}STABLE{Colors.white}]
 
    [7] Back
    """)
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        underdev()
        clearcmd()
        settings()

    elif USER_OPTION == "2":
        clearcmd()
        underdev()
        clearcmd()
        settings()

    elif USER_OPTION == "3":
        clearcmd()
        clearcache()

    elif USER_OPTION == "4":
        clearcmd()
        skip_intro()

    elif USER_OPTION == "5":
        clearcmd()
        timesettings()
    elif USER_OPTION == "6":
        clearcmd()
        discordrpcchange()
    elif USER_OPTION == "7":
        clearcmd()
        options()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        settings()
def discordrpcchange():
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
    ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
    ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
    ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
    ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
    ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝                                                                                                                                                                                                                                              
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"""
    [1] Enable Rich Presence
    [2] Disable Rich Presence
    
    [3] Back\n""")
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/discordrpc.txt", "w+") as file:
                file.write("YES")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully enabled Rich Presence, you may need to restard DrkGEN 2.0")
        back()
        clearcmd()
        try:
            settings()
        except AssertionError:
            print("Error found while turning on Discord RPC, ignoring error.")
            time.sleep(1)
            clearcmd()
            RPC.connect()
            settings()
    elif USER_OPTION == "2":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/discordrpc.txt", "w+") as file:
                file.write("NO")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully disabled Rich Presence, you may need to restard DrkGEN 2.0")
        back()
        clearcmd()
        settings()
    elif USER_OPTION == "3":
        clearcmd()
        settings()
def skip_intro():
    with open("./assets/skipintro.txt", "w+") as file:
            file.write("YES")
            file.close()
    clearcmd()
    time.sleep(0.3)
    print(f"{Colors.green}[+]{Colors.white} Sucessfully Turned on INTRO_SKIP.{Colors.white}")
    time.sleep(0.5)
    back()
    clearcmd()
    settings()

def timesettings():
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
    ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
    ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
    ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
    ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
    ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝                                                                                                                                                                                                                                              
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"""
    [1] 10 Seconds delay
    [2] 30 Seconds delay
    [3] 60 Seconds delay
    [4] 120 Seconds delay [Recommended]
    
    [5] 0 Second delay
    [6] Back\n""")
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/SleepTIME.txt", "w+") as file:
                file.write("10")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully changed SleepTIME to 10 Seconds.")
        back()
        clearcmd()
        settings()

    elif USER_OPTION == "2":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/SleepTIME.txt", "w+") as file:
                file.write("30")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully changed SleepTIME to 30 Seconds.")
        back()
        clearcmd()
        settings()

    elif USER_OPTION == "3":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/SleepTIME.txt", "w+") as file:
                file.write("60")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully changed SleepTIME to 60 Seconds.")
        back()
        clearcmd()
        settings()

    elif USER_OPTION == "4":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/SleepTIME.txt", "w+") as file:
                file.write("120")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully changed SleepTIME to 120 Seconds.")
        back()
        clearcmd()
        settings()

    elif USER_OPTION == "5":
        clearcmd()
        time.sleep(0.3)
        with open("./assets/SleepTIME.txt", "w+") as file:
                file.write("0")
                file.close()
        time.sleep(0.5)
        print(f"{Colors.green}[+]{Colors.white} Successfully changed SleepTIME to 0 Seconds.")
        back()
        clearcmd()
        settings()
    elif USER_OPTION == "6":
        clearcmd()
        options()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        settings()

        

def clearcache():
    print(Colorate.Horizontal(Colors.green_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})                       discord.gg/9y9HCzawBe
 ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██████╗     ██████╗ 
 ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ╚════██╗   ██╔═████╗
 ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║     █████╔╝   ██║██╔██║
 ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ██╔═══╝    ████╔╝██║
 ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗██╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝                        
                                                                          """))
    print(f'''                                 Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  ''')
    print("""
    [1] Clear Cache (THIS WILL REMOVE ALL YOUR GENERATED CODES!)

    [2] Back
    
    """)
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        time.sleep(0.3)
        open("./generated/amazon.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Amazon Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/apple.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Apple Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/googleplay.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Google Play Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/netflix.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Netflix Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/roblox.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Roblox Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/spotify.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Spotify Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/uber.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Uber Cache.{Colors.white}")
        time.sleep(0.3)
        open("./generated/steam.txt", "w").close()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared Steam Cache.{Colors.white}")
        time.sleep(1)
        clearcmd()
        print(f"{Colors.green}[+]{Colors.white} Sucessfully cleared cache.{Colors.white}")
        time.sleep(0.5)
        back()
        clearcmd()
        clearcache()

        
    elif USER_OPTION == "2":
        clearcmd()
        options()
        
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        options()

def options():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="In Main Menu - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )

    print(Colorate.Horizontal(Colors.green_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})                       discord.gg/9y9HCzawBe
 ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██████╗     ██████╗ 
 ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ╚════██╗   ██╔═████╗
 ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║     █████╔╝   ██║██╔██║
 ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ██╔═══╝    ████╔╝██║
 ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗██╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝                        
                                                                          """))
    print(f'''                                 Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  ''')
    print("""
    [1] Generators
    [2] Checkers

    [3] Credits/Support

    [4] Settings & Options
    [5] Quit
    
    
    """)
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        clearcmd()
        checkers()
    elif USER_OPTION == "3":
        clearcmd()
        credits()
    elif USER_OPTION == "4":
        clearcmd()
        settings()
    elif USER_OPTION == "5":
        clearcmd()
        RPC.close()
        quit()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        options()
def checkerudpnotice():
    clearcmd()
    print(f"{Colors.yellow}[?]{Colors.white} Make sure to use {Colors.purple}Settings/SleepTIME{Colors.white} to get the most accurate responses in UDPChecker.")
    back()
    clearcmd()
def checkerudp():
    with open("./assets/SleepTIME.txt", 'r+') as sleeptime:
        wait_chktime = 0
        amount = sleeptime.read()
        amount == float(amount)

    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Checking Giftcards - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )

    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    >=>     >=> >====>     >======>       >=>    >=>    >=> >=======>     >=>    >=>   >=>   
    >=>     >=> >=>   >=>  >=>    >=>  >=>   >=> >=>    >=> >=>        >=>   >=> >=>  >=>    
    >=>     >=> >=>    >=> >=>    >=> >=>        >=>    >=> >=>       >=>        >=> >=>     
    >=>     >=> >=>    >=> >======>   >=>        >=====>>=> >=====>   >=>        >>=>>       
    >=>     >=> >=>    >=> >=>        >=>        >=>    >=> >=>       >=>        >=>  >=>    
    >=>     >=> >=>   >=>  >=>         >=>   >=> >=>    >=> >=>        >=>   >=> >=>   >=>   
       >====>    >====>     >=>           >===>   >=>    >=> >=======>    >===>   >=>     >=> 
                                                                                           
    """))
    print(f"""{Colors.white}     [ Made by {Colors.blue}Nuhish#4697 {Colors.white}]{Colors.green} DRK GENERATOR PROJECT                              {Colors.white}{Colors.blue}SleepTIME = {amount}{Colors.white}
  {Colors.white}""")
    print(f"""
    [1] Amazon Checker [{Colors.yellow}UNSTABLE{Colors.white}]
    [2] Netflix Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [3] Roblox Checker [{Colors.yellow}UNSTABLE{Colors.white}]
    [4] Apple Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [5] Steam Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [6] Google Play Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [7] Spotfiy Checker [{Colors.yellow}UNSTABLE{Colors.white}]
    [8] Uber Checker [{Colors.yellow}UNSTABLE{Colors.white}]
    [9] Nintendo Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [10] NordVPN Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    [11] Bestbuy Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]
    
    // Discord Section
    [12] Discord Gift Link Checker [{Colors.red}UNDER DEVELOPMENT{Colors.white}]

    [13] Back
    """)

    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        checkerudpnotice()
        clearcmd()
        amazon_udp_check()
    elif USER_OPTION == "2":
        underdev()
        clearcmd()
        checkerudp()
    elif USER_OPTION == "3":
        checkerudpnotice()
        clearcmd()
        roblox_udp_check()
    elif USER_OPTION == "4":
        underdev()
        clearcmd()
        checkerudp()
    elif USER_OPTION == "5":
        underdev()
        clearcmd()
        checkerudp()
    elif USER_OPTION == "6":
        underdev()
        clearcmd()
        checkerudp()
    elif USER_OPTION == "7":
        checkerudpnotice()
        clearcmd()
        spotify_udp_check()
    elif USER_OPTION == "8":
        checkerudpnotice()
        clearcmd()
        uber_udp_check()
    elif USER_OPTION == "9":
        clearcmd()
        underdev()
        checkerudp()
    elif USER_OPTION == "10":
        clearcmd()
        underdev()
        checkerudp()
    elif USER_OPTION == "10":
        clearcmd()
        bestbuyudp()
    elif USER_OPTION == "12":
        clearcmd()
        underdev()
        checkerudp()
    elif USER_OPTION == "13":
        clearcmd()
        checkers()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        checkers()
    print("")
    input(f"\n{Colors.red}PRESS ENTER TO GO BACK.")

def bestbuyudp():
    pass
def tokengen():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating DCTokens - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
    print(Colorate.Horizontal(Colors.blue_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})          discord.gg/9y9HCzawBe
  _______    _               _____ ______ _   _ 
 |__   __|  | |             / ____|  ____| \ | |
    | | ___ | | _____ _ __ | |  __| |__  |  \| |
    | |/ _ \| |/ / _ \ '_ \| | |_ |  __| | . ` |
    | | (_) |   <  __/ | | | |__| | |____| |\  |
    |_|\___/|_|\_\___|_| |_|\_____|______|_| \_|                                                                                                                    
"""))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nDiscord Token Format is: {Colors.blue}[26 characters].[6 characters].[38 characters]")

    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many Discord Tokens do you want to generate, THIS WILL REMOVE PREVIOUS Codes: ")

    with open("./generated/discordtoken.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(26)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(38)))

            result = firstrandom + "." + secondrandom + "." + thirdrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Discord Tokens")
    back()
    clearcmd()
    discordsection()

def checkers():
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    ██████╗ ██████╗ ██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ ███████╗
    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
    ██║  ██║██████╔╝█████╔╝ ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝███████╗
    ██║  ██║██╔══██╗██╔═██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
    ██████╔╝██║  ██║██║  ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║███████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝                                                                                                                                                                                                                                               
    """))
    print(f"""                         Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print("""
    [1] DrkUDP (Single Connection)
    [2] DrkTCP (Proxies Required)

    [3] Back
    """)
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        checkerudp()
    elif USER_OPTION == "2":
        clearcmd()
        print(f"{Colors.red}[-]{Colors.white} DrkTCP is under development. Expect it ready by {Colors.yellow}V. 2.2{Colors.white}\n")
        back()
        clearcmd()
        checkers()
    elif USER_OPTION == "3":
        clearcmd()
        options()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        checkers()
    print("")
    input(f"\n{Colors.red}PRESS ENTER TO GO BACK.")
def credits():
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
     ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗    ██╗███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ██████╗ ████████╗
    ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝   ██╔╝██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
    ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗  ██╔╝ ███████╗██║   ██║██████╔╝██████╔╝██║   ██║██████╔╝   ██║   
    ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║ ██╔╝  ╚════██║██║   ██║██╔═══╝ ██╔═══╝ ██║   ██║██╔══██╗   ██║   
    ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║██╔╝   ███████║╚██████╔╝██║     ██║     ╚██████╔╝██║  ██║   ██║   
     ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝    ╚══════╝ ╚═════╝ ╚═╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                                                                                                              
    """))
    print(f"""                                 Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)

    print(f"""
    {Colors.green}DrkGEN 1.0 & DrkGEN 2.0{Colors.purple}
    ------------------------------------------------------------------------------------
    {Colors.purple}CREDITS
    ------------------------------------------------------------------------------------
    {Colors.white}
    {Colors.yellow}HEAD DEVELOPER {Colors.white}- {Colors.red}Nuhish#4697
    
    {Colors.purple}#####################################################

    {Colors.yellow}Helper {Colors.white}- {Colors.red}.mrduckman345
    {Colors.yellow}Helper {Colors.white}- {Colors.red}avk_llo
    {Colors.yellow}Helper {Colors.white}- {Colors.red}piixelll_

    {Colors.purple}#####################################################

    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} wallet#0323
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} Sporkxx#0001
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} 240SX#8662
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} CHRIS?#0001
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} floop#5806
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} nick#2789
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} TETI#0676
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} Truth#5052
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} xxjakobxx#0498
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} ZoinksBoinksFoinks#8714
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} saint/coltin
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} BllzAreGay
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} Snordakson
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} dukeletoii
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} KillerBee
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} karmaqueen2018
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} adelpha!
    {Colors.yellow}Beta Tester {Colors.white}-{Colors.red} KPRI

    
    
    ------------------------------------------------------------------------------------
    {Colors.purple}SUPPORT & DISCORD
    ------------------------------------------------------------------------------------
    {Colors.white}SUPPORT: {Colors.yellow}discord.gg/9y9HCzawBe (open a support ticket or contact me)

    """)
    input(f"\n{Colors.red}PRESS ENTER TO GO BACK.")
    clearcmd()
    options()

def generators():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Giftcards - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    print(Colorate.Horizontal(Colors.green_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})                       discord.gg/9y9HCzawBe
 ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██████╗     ██████╗ 
 ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ╚════██╗   ██╔═████╗
 ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║     █████╔╝   ██║██╔██║
 ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ██╔═══╝    ████╔╝██║
 ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗██╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝                        
                                                                          """))
    print(f'''                                                         Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  ''')
    print(f"""
    [1] INTER Amazon Giftcard Generator [{Colors.green}STABLE{Colors.white}] {Colors.yellow}[Region Chocies]{Colors.white}
    [2] EU Netflix Giftcard Generator [{Colors.green}STABLE{Colors.white}]
    [3] INTER Roblox Giftcard Generator [{Colors.green}STABLE{Colors.white}] 
    [4] US Apple Giftcard Generator [{Colors.green}STABLE{Colors.white}]
    [5] INTER Steam Giftcard Generator [{Colors.green}STABLE{Colors.white}]
    [6] EU Google Play Giftcard Generator [{Colors.green}STABLE{Colors.white}] {Colors.yellow}[Balance Chocies]{Colors.white}
    [7] INTER Spotfiy Giftcard Generator [{Colors.green}STABLE{Colors.white}]
    [8] INTER Uber Giftcard Generator [{Colors.green}STABLE{Colors.white}]
    [9] INTER Nintendo Giftcard Generator [{Colors.green}STABLE{Colors.white}] {Colors.yellow}[Region Chocies]{Colors.white}
    [10] INTER NordVPN Activation Code Generator [{Colors.green}STABLE{Colors.white}]   
    [11] EU Paysafecard Code Generator [{Colors.yellow}UNSTABLE{Colors.white}] 
    
    [12] Discord Section
    [13] Info

    [14] Go back
    
    
    """)
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        amazon()
    elif USER_OPTION == "2":
        clearcmd()
        netflix()
    elif USER_OPTION == "3":
        clearcmd()
        roblox()
    elif USER_OPTION == "4":
        clearcmd()
        apple()
    elif USER_OPTION == "5":
        clearcmd()
        steam()
    elif USER_OPTION == "6":
        clearcmd()
        googleplay()
    elif USER_OPTION == "7":
        clearcmd()
        spotify()
    elif USER_OPTION == "8":
        clearcmd()
        uber()
    elif USER_OPTION == "9":
        clearcmd()
        nintendosection()
    elif USER_OPTION == "10":
        clearcmd()
        nordvpngen()
    elif USER_OPTION == "11":
        clearcmd()
        paysafegen()
    elif USER_OPTION == "12":
        clearcmd()
        discordsection()
    elif USER_OPTION == "13":
        clearcmd()
        geninfo()
    elif USER_OPTION == "14":
        clearcmd()
        options()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        generators()

def paysafegen():
    pass

def nordvpngen():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating NordVPN - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
    print(Colorate.Horizontal(Colors.blue_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})          discord.gg/9y9HCzawBe
  _   _               ___      _______  _   _    _____            
 | \ | |             | \ \    / /  __ \| \ | |  / ____|           
 |  \| | ___  _ __ __| |\ \  / /| |__) |  \| | | |  __  ___ _ __  
 | . ` |/ _ \| '__/ _` | \ \/ / |  ___/| . ` | | | |_ |/ _ \ '_ \ 
 | |\  | (_) | | | (_| |  \  /  | |    | |\  | | |__| |  __/ | | |
 |_| \_|\___/|_|  \__,_|   \/   |_|    |_| \_|  \_____|\___|_| |_|                                                                                                                     
"""))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nNordVPN Activation Code Format is: {Colors.blue}NVXREVXXXXXXXXXXXXXXXXXXX")

    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many Activation codes do you want to generate, THIS WILL REMOVE PREVIOUS Codes: ")

    with open("./generated/nordvpn.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(1)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(19)))

            result = "NV" + firstrandom + "REV" + secondrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} NordVPN Activation Codes.")
    back()
    clearcmd()
    generators()
def nintendosection():
    print(Colorate.Horizontal(Colors.green_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})                       discord.gg/9y9HCzawBe
 ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██████╗     ██████╗ 
 ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ╚════██╗   ██╔═████╗
 ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║     █████╔╝   ██║██╔██║
 ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ██╔═══╝    ████╔╝██║
 ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗██╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝                        
                                                                          """))
    print(f'''                                                         Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  ''')
    
    print("""[1] UK Nintendo Giftcard Generator
[2] Under Development (Lack of Details)
[3] Under Development (Lack of Details)
[4] Under Development (Lack of Details)
          
[5] Back
""")
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        nintendo1()
    elif USER_OPTION == "2":
        underdev()
        nintendosection()
    elif USER_OPTION == "3":
        underdev()
        nintendosection()
    elif USER_OPTION == "4":
        underdev()
        nintendosection()
    elif USER_OPTION == "5":
        clearcmd()
        generators()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        generators()
def nintendo1():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Nintendo - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.blue_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})    discord.gg/9y9HCzawBe
  _   _ _       _                 _          _____            
 | \ | (_)     | |               | |        / ____|           
 |  \| |_ _ __ | |_ ___ _ __   __| | ___   | |  __  ___ _ __  
 | . ` | | '_ \| __/ _ \ '_ \ / _` |/ _ \  | | |_ |/ _ \ '_ \ 
 | |\  | | | | | ||  __/ | | | (_| | (_) | | |__| |  __/ | | |
 |_| \_|_|_| |_|\__\___|_| |_|\__,_|\___/   \_____|\___|_| |_|                                                                                                                        
"""))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nNintendo UK Giftcard Format is: {Colors.blue}C0XXXXXXXXXXXXXX")

    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many Giftcards do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/nintendo.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(14)))

            result = "C0" + firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Nintendo UK Giftcard")
    back()
    clearcmd()
    generators()
def discordsection():
    print(Colorate.Horizontal(Colors.green_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})                       discord.gg/9y9HCzawBe
 ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██████╗     ██████╗ 
 ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ╚════██╗   ██╔═████╗
 ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║     █████╔╝   ██║██╔██║
 ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ██╔═══╝    ████╔╝██║
 ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗██╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝ ╚═════╝                        
                                                                          """))
    print(f'''                                                         Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  ''')
    
    print("""[1] Nitro Gift Generator
[2] Discord Token Generator
[3] To be added
[4] To be added
          
[5] Back
""")
    USER_OPTION = input(f"Option\n{Colors.red}>")
    if USER_OPTION == "1":
        clearcmd()
        discordgift()
    elif USER_OPTION == "2":
        clearcmd()
        tokengen()
    elif USER_OPTION == "3":
        underdev()
        discordsection()
    elif USER_OPTION == "4":
        underdev()
        discordsection()
    elif USER_OPTION == "5":
        clearcmd()
        generators()
def discordgift():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating DiscordGift - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.blue_to_red, f"""
 V. 0.857 CLOSED BETA ({now.year}-{now.month}-{now.day})    discord.gg/9y9HCzawBe
  _____  _                       _    _____ _  __ _   
 |  __ \(_)                     | |  / ____(_)/ _| |  
 | |  | |_ ___  ___ ___  _ __ __| | | |  __ _| |_| |_ 
 | |  | | / __|/ __/ _ \| '__/ _` | | | |_ | |  _| __|
 | |__| | \__ \ (_| (_) | | | (_| | | |__| | | | | |_ 
 |_____/|_|___/\___\___/|_|  \__,_|  \_____|_|_|  \__|
                                                                                             
"""))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\Discord Gift Link Format is: {Colors.blue}https://discord.com/gifts/GIFT_CARD_HERE\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many Gift Links do you want to generate, THIS WILL REMOVE PREVIOUS LINKS: ")

    with open("./generated/discordgift.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = "https://discord.com/gifts/" + firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Discord Gift Link")
    back()
    clearcmd()
    generators()
    
def uber():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Uber - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBS = "1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
     #     #                          #####  ####### #     # 
     #     # #####  ###### #####     #     # #       ##    # 
     #     # #    # #      #    #    #       #       # #   # 
     #     # #####  #####  #    #    #  #### #####   #  #  # 
     #     # #    # #      #####     #     # #       #   # # 
     #     # #    # #      #   #     #     # #       #    ## 
      #####  #####  ###### #    #     #####  ####### #     # 
                                                                                                                         
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nUber Giftcard Format is: {Colors.blue}XXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/uber.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))
            secondrandom = ''.join(random.choice(NUMBS) for i in range(int(6)))

            result = firstrandom + secondrandom 
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards")
    back()
    clearcmd()
    generators()

def geninfo():
    print("Generators are all random, this will not 100 procent give accurate codes. It is all random, thats why there is DrkGEN/Checkers. Any use of this product I am not responsible for!")
    back()
    clearcmd()
    generators()
def amazon():
    print("""[1] UK Amazon Card
[2] EU Amazon Card
[3] US Amazon Card
[4] CA Amazon Card
          
[5] Back
""")
    USER_OPTION = input(f"{Colors.blue}[?] Region of Giftcard:\n{Colors.red}>{Colors.white} ")
    if USER_OPTION == "1":
        clearcmd()
        amazonUK()
    elif USER_OPTION == "2":
        with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
            answer = DISCORD_RPC_FILE.read()
            if answer == "NO":
                clearcmd()
            else:
                RPC.update(
                    state="Generating Amazon - V. 0.857 BETA",
                    large_image="icon",
                    buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
                )
        clearcmd()
        CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        print(Colorate.Horizontal(Colors.green_to_red,"""
        DrkGEN 2.0 (V. 0.857)
        █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
        ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
        ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
        ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
        ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
        ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
        """))
        print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
    """)
        print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
        time.sleep(1)
        print(f"\nAmazon Giftcard Format is: {Colors.blue}XXXX-XXXXXX-XXXXX\n")
        howmany = input(f"{Colors.red}{curtime} {Colors.blue}Amount of cards to generate:{Colors.white}")

        with open("./generated/amazon.txt", "w+") as file:
            for i in range(int(howmany)):
                firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
                secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
                thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

                result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
                file.write(result)
                file.write("\n")
        print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
        time.sleep(1)
        file.close()
        print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards")
        back()
        clearcmd()
        generators()
    elif USER_OPTION == "3":
        clearcmd()
        amazonUS()
    elif USER_OPTION == "4":
        clearcmd()
        amazonCA()
    elif USER_OPTION == "5":
        clearcmd()
        generators()
    else:
        print(f"\n{Colors.red}[-]{Colors.white} Did not reckognize input {Colors.blue}{USER_OPTION}{Colors.white}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        generators()

def amazonUS():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Amazon - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nAmazon Giftcard Format is: {Colors.blue}XXXX-XXXXX-XXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}Amount of cards to generate:{Colors.white}")

    with open("./generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Amazon US Giftcards")
    back()
    clearcmd()
    generators()
def amazonCA():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Amazon - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nAmazon Giftcard Format is: {Colors.blue}XXXX-XXXXXX-XXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}Amount of cards to generate:{Colors.white}")

    with open("./generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Amazon CA Giftcards")
    back()
    clearcmd()
    generators()
def amazonUK():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Amazon - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
""")
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nAmazon Giftcard Format is: {Colors.blue}XXXX-XXXXXX-XXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}Amount of cards to generate:{Colors.white}")

    with open("./generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Amazon UK Giftcards")
    back()
    clearcmd()
    generators()
def netflix():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Netflix - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
    ███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                            
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nNetflix Giftcard Format is: {Colors.blue}XXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/netflix.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(11)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/netflix.txt")
    back()
    clearcmd()
    generators()

def roblox():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Roblox - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
    ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║       
    ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                       
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nRoblox Giftcard Format is: {Colors.blue}RXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/roblox.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(17)))
            result = "R" + firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/roblox.txt")
    back()
    clearcmd()
    generators()

def apple():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Apple - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
     █████╗ ██████╗ ██████╗ ██╗     ███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██████╔╝██████╔╝██║     █████╗      ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║     ██║     ███████╗███████╗    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                   
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nApple Giftcard Format is: {Colors.blue}XXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/apple.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(15)))

            result = "X" + firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/apple.txt")
    back()
    clearcmd()
    generators()

def steam():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Steam - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
    ███████╗████████╗███████╗ █████╗ ███╗   ███╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗   ██║   █████╗  ███████║██╔████╔██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║    ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                               
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nSteam Giftcard Format is: {Colors.blue}XXXXX-XXXXX-XXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/steam.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(16)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/steam.txt")
    back()
    clearcmd()
    generators()

def googleplay():
    print("""[1] $10 Google Play Card
[2] $100 EU Google Play Card
          
[3] Back""")
    USER_OPTION = input(f"{Colors.blue}[?] Region of Giftcard:\n{Colors.red}>{Colors.white} ")
    if USER_OPTION == "1":
       clearcmd()
       googleplay1()
    elif USER_OPTION == "2":
       clearcmd()
       googleplay2()
    elif USER_OPTION == "3":
       clearcmd()
       generators()

def googleplay1():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating GooglePlay - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗      ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗█████╗██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝╚════╝██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██║         ╚██████╔╝███████╗██║ ╚████║                                                                                                                                                                                                                                                                                                                                                                                                                                       
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nGoogle Play Giftcard Format is: {Colors.blue}XXXXXXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/googleplay.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(20)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/googleplay.txt")
    back()
    clearcmd()
    generators()

def googleplay2():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating GooglePlay - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ██████╗      ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗█████╗██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝╚════╝██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ██║         ╚██████╔╝███████╗██║ ╚████║                                                                                                                                                                                                                                                                                                                                                                                                                                       
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\nGoogle Play Giftcard Format is: {Colors.blue}XXXXXXXXXXXXXXXXXXXXX\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/googleplay.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(21)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/googleplay.txt")
    back()
    clearcmd()
    generators()

def spotify():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Generating Spotify - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(Colorate.Horizontal(Colors.green_to_red,"""
     DrkGEN 2.0 (V. 0.857)
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ╚██████╔╝███████╗██║ ╚████║
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}
  """)
    print(f"{Colors.blue}[*]{Colors.white} Setting Up...")
    time.sleep(1)
    print(f"\Spotify Giftcard Format is: {Colors.blue}XXX XXX XXX Xx\n")
    howmany = input(f"{Colors.red}{curtime} {Colors.blue}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/spotify.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(11)))

            result = firstrandom
            file.write(result)
            file.write("\n")
    print(f"{Colors.red}{curtime} {Colors.blue}[*]{Colors.white} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Colors.red}{curtime} {Colors.green}[+]{Colors.white} Successfully generated {Colors.blue}{howmany}{Colors.white} Giftcards in ./generated/spotfiy.txt")
    back()
    clearcmd()
    generators()

def license():
    # keys = requests.get("http://drksoftware.store/drkgenkeys.txt").text
    
    # keyfromuser = input(f"{Colors.yellow}Enter your key\n{Colors.red}>{Colors.white}")

    # for key in keys.splitlines():
        # if key == keyfromuser:
            # clearcmd()
            # print(f"{Colors.green}Logging in.")
            # time.sleep(0.5)
            # return
    # if keyfromuser == "betadrk":
        # clearcmd()
        # print(f"{Colors.green}Logging in.")
        # time.sleep(0.5)
        # return            
    key = "betatest"

    keyfromuser = input(f"{Colors.yellow}Enter your key\n{Colors.red}>{Colors.white}")
    if key == keyfromuser:
        clearcmd()
        print(f"{Colors.green}Logging in.")
        time.sleep(0.5)
        return
    
    print(f"\n{Colors.red}Your key \"{Colors.yellow}{keyfromuser}\"{Colors.red} is invalid.{Colors.white}")
    input("\nPress ENTER to try again.")
    clearcmd()
    license()


## CHECKERS
def udpart():
    print(Colorate.Horizontal(Colors.green_to_red,"""
    DrkGEN 2.0 (V. 0.857)
    >=>     >=> >====>     >======>       >=>    >=>    >=> >=======>     >=>    >=>   >=>   
    >=>     >=> >=>   >=>  >=>    >=>  >=>   >=> >=>    >=> >=>        >=>   >=> >=>  >=>    
    >=>     >=> >=>    >=> >=>    >=> >=>        >=>    >=> >=>       >=>        >=> >=>     
    >=>     >=> >=>    >=> >======>   >=>        >=====>>=> >=====>   >=>        >>=>>       
    >=>     >=> >=>    >=> >=>        >=>        >=>    >=> >=>       >=>        >=>  >=>    
    >=>     >=> >=>   >=>  >=>         >=>   >=> >=>    >=> >=>        >=>   >=> >=>   >=>   
       >====>    >====>     >=>           >===>   >=>    >=> >=======>    >===>   >=>     >=> 
                                                                                           
    """))
    print(f"""Logged in as {Colors.blue}{keyauthapp.user_data.username}{Colors.white}""")

def amazon_udp_check():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Checking Amazon - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    with open("./assets/SleepTIME.txt", 'r+') as sleeptime:
        wait_chktime = 0
        amount = sleeptime.read()
        amount == float(amount)
    clearcmd()
    udpart()
    with open("./generated/amazon.txt", 'r') as file:
        li = file.readlines()
    cnt = len(li)
    print(f"{Colors.yellow}[?]{Colors.white} Checking {Colors.blue}{int(cnt)} {Colors.white}Amazon giftcards.")
    time.sleep(2)
    clearcmd()
    invalid = 0
    valid = 0
    success_keyword = """ <b>Enter claim code</b> """
    with open("./generated/amazon.txt", 'r+') as gcfile:
        giftcard = gcfile.readlines()
        for key in giftcard:
            key.strip()
            r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": key})
            if success_keyword in r.text:
                print(f"{Colors.green}[+]{Colors.white} {key} is valid.")
                valid += 1
            else:
                print(f"{Colors.red}[-]{Colors.white} KEY is invalid. [UDP CHECKS LIMIT EVERY 5 REQUESTS!] KEY: {Colors.red}{key}{Colors.white}")
                invalid += 1
                time.sleep(int(amount))
                print(f"{Colors.yellow}[?]{Colors.white} Waiting for {int(amount)} Seconds.")
        print(f"{Colors.yellow}[!]{Colors.white} There were in total {invalid}{Colors.red} invalids{Colors.white} and {valid}{Colors.green} valids{Colors.white}")
        back()
        clearcmd()
        checkerudp()

def netflix_udp_check():
    clearcmd()
    udpart()
def uber_udp_check():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Checking Uber - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    udpart()
    with open("./generated/uber.txt", 'r') as file:
            li = file.readlines()
            cnt = len(li)
            print(f"{Colors.yellow}[?]{Colors.white} Checking {Colors.blue}{int(cnt)} {Colors.white}Uber giftcards.")
            time.sleep(2)
            clearcmd()

    with open("./generated/uber.txt", 'r+') as gcfile:
            giftcard = gcfile.readlines()
            valid = 0
            success_keyword = "200"
            for key in giftcard:
                key.strip()
                r = requests.post(f"https://vouchers.uber.com/redeem/{key}?source=alreadyLoggedIn")
                if success_keyword in r.text:
                    print(f"{Colors.green}[+]{Colors.white} {key} is valid.")
                    float(valid + 1)
                else:
                    print(f"{Colors.red}[-]{Colors.white} KEY is invalid. [UDP CHECKS LIMIT EVERY 5 REQUESTS!] KEY: {Colors.red}{key}{Colors.white}")
                    
            print(f"{Colors.yellow}[!]{Colors.white} There were in total {invalid}{Colors.red} invalids{Colors.white} and {valid}{Colors.green} valids{Colors.white} {Colors.yellow}(MAY SHOW WRONG NUMBERS (BETA){Colors.white}")
            back()
            clearcmd()
            checkerudp()        
def apple_udp_check():
    clearcmd()
    udpart()
    
def steam_udp_check():
    clearcmd()
    udpart()
    with open("./generated/uber.txt", 'r') as file:
            li = file.readlines()
            cnt = len(li)
            print(f"{Colors.yellow}[?]{Colors.white} Checking {Colors.blue}{int(cnt)} {Colors.white}Uber giftcards.")
            time.sleep(2)
            clearcmd()
    with open("./assets/SleepTIME.txt", 'r+') as sleeptime:
        amount = sleeptime.read()
        amount == float(amount)

    with open("./generated/uber.txt", 'r+') as gcfile:
            giftcard = gcfile.readlines()
            valid = 0
            invalid = 0
            success_keyword = "200"
            for key in giftcard:
                key.strip()
                r = requests.post(f"https://vouchers.uber.com/redeem/{key}?source=alreadyLoggedIn")
                if success_keyword in r.text:
                    print(f"{Colors.green}[+]{Colors.white} {key} is valid.")
                    valid += 1
                else:
                    print(f"{Colors.red}[-]{Colors.white} KEY is invalid. [UDP CHECKS LIMIT EVERY 5 REQUESTS!] KEY: {Colors.red}{key}{Colors.white}")
                    invalid += 1
                    time.sleep(int(amount))
                    print(f"{Colors.yellow}[?]{Colors.white} Waiting for {int(amount)} Seconds.")
                    
            print(f"{Colors.yellow}[!]{Colors.white} There were in total {invalid}{Colors.red} invalids{Colors.white} and {valid}{Colors.green} valids{Colors.white}")
            back()
            clearcmd()
            checkerudp()  

def googleplay_udp_check():
    clearcmd()
    udpart()
def spotify_udp_check():
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Checking Spotify - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    udpart()
    api = "https://www.spotify.com/se/redeem/v2/api/redeem/"
    capkey = "03AFcWeA405w8QjpyjZS-YAqt-mfM-wRPVqLvBZPGryvOQcJkf_hFJtODdNugY5C8-wWKlF2SC4ZlLSz6mwsWqb-WGCQ_njhCotaF_Tm7dX1WMOCcxeue5sgupDaWrQSVYYMankk5_Qw5dl7yN05fj2Pyt7R4Iv_V68pzOiEgFOrAQZ76jDsioZnQ_7FOfoqBzTPG1InLlQFsFHMVtPl_l9YqyBmuNyUCkbyBpEWHGpTOkyBOVAeGwxBmf0NAziOhyWHd8TWTvOUJHmWsjuQ5harIRqj-T6AozttY9MVnCDqbXx9tmZCEizE-OFC2HX_m49J8leH7kPi-yAnQkaiHDjSO67wrvCWu2-QNyh8HdWwhd0_rjoYbpOzv0Q29EGz1F33H_ZCwVsD3BR53R2l53vv9snQcrdl1KIGh195rc0XBhCjBtZpzT1MjUphyQe_t6c4C8JXAyfCXEsuk1nY5e2YGXpsgHyxg1AGnz2Dcyb_tA7tXSplGbvqiazNgc_lLc87H5xpeJvgmhVBPC0Lkm3OIuN0vEZTpwi6YDNOG5btjK2L0sFKrwuFyh3MWqvNF8nOLE9rSjeCtByL13rONhSRjZtzO9JFt5FA"
    with open("./generated/spotify.txt", 'r') as file:
        li = file.readlines()
    cnt = len(li)
    print(f"{Colors.yellow}[?]{Colors.white} Checking {Colors.blue}{int(cnt)} {Colors.white}Spotify giftcards.")
    time.sleep(2)
    clearcmd()

    with open("./assets/SleepTIME.txt", 'r+') as sleeptime:
        wait_chktime = 0
        amount = sleeptime.read()
        amount == float(amount)

    success_keyword = """https://spotify.com/account"""
    invalid = 0
    valid = 0
    with open("./generated/spotify.txt", 'r+') as gcfile:
        giftcard = gcfile.readlines()
        for key in giftcard:
            key.join(key.split())
            r = requests.post(api, data={"token": key, "recaptchakey": capkey})
            if success_keyword in r.text:
                print(f"{Colors.green}[+]{Colors.white} {key} is valid.")
                valid += 1
            else:
                print(f"{Colors.red}[-]{Colors.white} KEY is invalid. [UDP CHECKS LIMIT EVERY 5 REQUESTS!] KEY: {Colors.red}{key}{Colors.white}")
                invalid += 1
                time.sleep(wait_chktime)
                print(f"{Colors.yellow}[?]{Colors.white} Waiting for {wait_chktime} Seconds.")
        print(f"{Colors.yellow}[!]{Colors.white} There were in total {invalid}{Colors.red} invalids{Colors.white} and {valid}{Colors.green} valids{Colors.white}")
        back()
        clearcmd()
        checkerudp()
def roblox_udp_check():
    with open("./assets/SleepTIME.txt", 'r+') as sleeptime:
        wait_chktime = 0
        amount = sleeptime.read()
        amount == float(amount)
    with open("./assets/discordrpc.txt", 'r+') as DISCORD_RPC_FILE:
        answer = DISCORD_RPC_FILE.read()
        if answer == "NO":
            clearcmd()
        else:
            RPC.update(
                state="Checking Roblox - V. 0.857 BETA",
                large_image="icon",
                buttons=[{"label": "Check Project out!", "url": "https://discord.gg/9y9HCzawBe"}]
            )
    clearcmd()
    udpart()
    api = "https://billing.roblox.com/v1/credit"
    with open("./generated/roblox.txt", 'r') as file:
        li = file.readlines()
    cnt = len(li)
    print(f"{Colors.yellow}[?]{Colors.white} Checking {Colors.blue}{int(cnt)} {Colors.white}Roblox giftcards.")
    time.sleep(2)
    clearcmd()
    success_keyword = """true"""
    with open("./generated/roblox.txt", 'r+') as gcfile:
        giftcard = gcfile.readlines()
        valid = 0
        invalid = 0
        for key in giftcard:
            key.join(key.split())
            r = requests.post(api, data={"code": key})
            if success_keyword in r.text:
                print(f"{Colors.green}[+]{Colors.white} {key} is valid.")
                valid += 1
            else:
                print(f"{Colors.red}[-]{Colors.white} KEY is invalid. [UDP CHECKS LIMIT EVERY 5 REQUESTS!] KEY: {Colors.red}{key}{Colors.white}")
                invalid += 1
                print(f"{Colors.yellow}[?]{Colors.white} Waiting for {int(amount)} Seconds.")
                time.sleep(int(amount))
                continue
            print(f"{Colors.yellow}[!]{Colors.white} There were in total {invalid}{Colors.red} invalids{Colors.white} and {valid}{Colors.green} valids{Colors.white}")
        back()
        clearcmd()
        checkerudp()





# Main Code
def main():
    try:
        clearcmd()
        keyauthtry()
        clearcmd()
        with open("./assets/skipintro.txt", 'r+') as INTRO_SKIP_FILE:
            answer = INTRO_SKIP_FILE.read()
            if answer == "YES":
                clearcmd()
                options()
            else:
                pass



        print(f"{Colors.blue}[*] Starting DrkGEN 2.0")

        time.sleep(1.5)
        clearcmd()
        print(f"""
                                {Colors.red}LICENSE AGREEMNT\n{Colors.white}
                            GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007

        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
        Everyone is permitted to copy and distribute verbatim copies
        of this license document, but changing it and removing credits is not allowed.

        {Colors.blue}https://github.com/DrkTheDon/BlackDC/blob/main/LICENSE
        """)
        time.sleep(3.3)
        clearcmd()
        clearcmd()
        options()
    except KeyboardInterrupt:
        print(f"{Colors.red}{curtime} CTRL + C detected, Going back to the main menu!")
        time.sleep(1)
        options()

main()
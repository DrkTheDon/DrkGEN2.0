#!/usr/bin/python3

#####################################################
## ProxyFormatter (DrkGen)                         ##
## Formats Proxies for DrkGEN 2.0                  ##
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

# DEFINES
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')



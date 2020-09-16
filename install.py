import os
import time
import sys, random

os.system('apt install python2 -y && apt install python3')
os.system('pip3 install queue')
os.system('pip3 install request')
os.system('pip3 install socket')

#accept
print ("[!] Starting Trojan...")
time.sleep(3)
os.system('clear')
os.system('python3 trojan.py')

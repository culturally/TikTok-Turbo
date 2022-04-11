from os import system
import os
import time 
from colorama import Fore, Back, Style
import sys
import json
import random
import warnings
import threading
import urllib3
from urllib.parse import urlencode
import threading
from threading import Thread
import ctypes

if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)


http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False) #disabled ssl cert verification
#default_headers = make_headers(proxy_basic_auth='myusername:mypassword') if wanna use proxy(you most likely will need and use some rotating proxy to bypass rate limit
#http = ProxyManager("https://myproxy.com:8080/", headers=default_headers)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')#disabled warnings
attempts=0
banner = '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"'
system("title " + "t.me/undecryptable")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + banner)
print('')
user = input(Back.BLACK + Fore.WHITE + " Enter @")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + banner)
print(Fore.CYAN + '          Session ID')
print('')
print('')
sid = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + banner)
print(Fore.CYAN + '          Threads')
print('')
print('')
threads = int(input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"yin" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" "))
ctypes.windll.user32.MessageBoxW(0, "Starting...", "yin", 0)
os.system('cls||clear')






def tachyon():  
    global attempts    
    system("title " + f"Attempts ~ {attempts}")
    url='https://api16-normal-c-useast1a.tiktokv.com/passport/login_name/update/?residence=RU&device_id=6916380144430155270&os_version=15.2&multi_login=1&app_id=1233&iid=7027499342660585222&app_name=musical_ly&vendor_id=8F5E8D11-F4F1-4184-BFAA-732A6E7CF25B&locale=en&ac=WIFI&sys_region=CA&js_sdk_version=1.77.0.2&ssmix=a&version_code=21.7.0&vid=8F5E8D11-F4F1-4184-BFAA-732A6E7CF25B&channel=App%20Store&op_region=RU&tma_jssdk_version=1.77.0.2&os_api=18&idfa=12E61037-060B-46C3-AC5D-E10C3E11497A&install_id=7027499342660585222&idfv=12E61037-060B-46C3-AC5D-E10C3E11497A&device_platform=ipad&device_type=iPad8%2C11&openudid=18dc3b90ebb7bff5930ba0b5948e374d8ca4fe52&account_region=&tz_name=Europe%2FMoscow&tz_offset=3600&app_language=en&current_region=RU&build_number=218032&aid=1233&mcc_mnc=&screen_width=1620&uoo=0&content_language=&language=en&cdid=66C6FDB8-73B5-45A9-9E65-72FB05BB91E9&app_version=21.7.0&resolution=2160%2A1620&cronet_version=b9766152_2021-07-19&ttnet_version=4.0.61.2'#TIKTOK API ENDPOINT
    data = {'login_name': user} 
    encoded_data = urlencode(data)
    res = http.request(
        'POST',
        url,
        body=encoded_data,
        headers={
        'Connection' : 'keep-alive',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Cookie': f'sessionid={sid}',
        'x-tt-passport-csrf-token' : f'{sid}',
        'Host' : 'api16-normal-c-useast1a.tiktokv.com',
        'passport-sdk-version' : '5.12.1',
        'sdk-version' : '2',
        'user-agent' : 'TikTok 21.7.0 rv:217018 (iPad; iOS 15.2; en_CA) Cronet'
        })
    attempts+=1
    #print(res.data.decode('utf-8'))
    if '"message":"success"' in res.data.decode('utf-8'): #feel free to mess with this shit
        print(Back.BLACK + Fore.GREEN + f'\nSuccesfully swapped @{user.strip()}'+ Back.BLACK + Fore.WHITE)
        print('\n\t by yin @undecryptable')
        sys.exit()
    elif 'login name can only be updated once within one month.' in res.data.decode('utf-8'):
        print(Back.BLACK + Fore.YELLOW + f'\nNot Possible to change username(delay)' + Back.BLACK + Fore.WHITE)
        sys.exit()
    elif 'Only letters, numbers, underscores, or periods are allowed' in res.data.decode('utf-8'):
        sys.exit()
    #elif '"description":"This username is taken, but you can try a different one"' in res.data.decode('utf-8'):
    
    #elif '"description":"Too many attempts. Try again later."' in res.data.decode('utf-8'):
    
if type(threads) == int: #smart print ;)
    print(Fore.WHITE + '[' + Fore.MAGENTA + '+' + Fore.WHITE + ']' + f'Target ~ {Fore.MAGENTA}@{user}')
    print(Fore.WHITE + '[' + Fore.MAGENTA + '+' + Fore.WHITE + ']' + f'SessionID ~ {Fore.MAGENTA}{sid}')
    print(Fore.WHITE + '[' + Fore.MAGENTA + '+' + Fore.WHITE + ']' + f'Threads ~ {Fore.MAGENTA} {threads}')
     
    
    
tag=True

while tag == True: #just an animation
    print(Fore.WHITE + '\r[' + Fore.MAGENTA + '\\' + Fore.WHITE + ']' + Fore.MAGENTA + 'yin' + Fore.WHITE, end='')
    time.sleep(0.1)
    print(Fore.WHITE + '\r[' + Fore.MAGENTA + '/' + Fore.WHITE + ']' + Fore.MAGENTA + 'yin' + Fore.WHITE, end='')
    for i in range(threads):
        [].append(threading.Thread(target=tachyon).start())
    for threadz in []:
        threadz.join()

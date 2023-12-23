import os
import webbrowser
import requests;from requests import get
import time
from urllib import request as urlrequest
from itertools import cycle
import traceback
import threading;from threading import Thread
import random
import sys
from faker import Faker
import time
import string
import socket
import random
from urllib.parse import urlparse
import socket
import json

from colorama import init
init()
from colorama import Fore, Back, Style   

print("\n")
url = input("Domain: ")
list = []

def wordlists_brute_force():
    try:
        def wordlist_1():
            try:
                urllist = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-110000.txt"
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                    else:
                                        print(url_subdomain,":",ip)
                                        
                            if r.status_code == 404:
                                
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)

                            if r.status_code == 301:
                                
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)                   
                        except:
                            pass
            except:
                return
                
        def wordlist_2():
            try:
                urllist = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/shubs-subdomains.txt"
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                    else:
                                        print(url_subdomain,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
              
                        except:
                            pass
            except:
                return




        def wordlist_3():
            try:
                urllist = "https://raw.githubusercontent.com/danTaler/WordLists/master/Subdomain.txt"  
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                    else:
                                        print(url_subdomain,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                                    
                                        
                        except:
                            pass
            except:
                return

        def wordlist_4():

            try:
                urllist = "https://raw.githubusercontent.com/rajesh6927/subdomain-bruteforce-wordlist/main/Subdomain-wordlist.txt"  
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                    else:
                                        print(url_subdomain,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)

                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                                    
                                        
                        except:
                            pass
            except:
                return
                
        def wordlist_5():
            try:
                
                urllist = "https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/directory_scanner/top_subdomains.txt"   
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE+"==>"+response.url)
                                    else:
                                        print(url_subdomain,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)
                                    
                            if r.status_code == 301:
                                
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                                    
                                        
                        except:
                            pass
            except:
                return

        def wordlist_6():
            try:
                urllist = "https://raw.githubusercontent.com/emadshanab/wordlists/master/common_subs_nl.txt"    
                r = requests.get(urllist, stream=True)
                for line in r.iter_lines():
                    if line:
                        string = line
                        string = str(string)
                        string = string.replace("b","")
                        string = string.replace("'","")
                        url_subdomain = "https://"+string+"."+url
                        string = url_subdomain
                        string = str(string)
                        string = string.replace("https://","")
                        string=string.replace("http://","")
                        no_hp_sub = string
                        try:
                            r = requests.get(url_subdomain)
                            if r.status_code == 200:

                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    if "Cloudflare, Inc." in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                    elif "Amazon" in string:
                                        print(url_subdomain,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                    else:
                                        print(url_subdomain,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)              
                        except:
                            pass
            except:
                return


        word1 = threading.Thread(target=wordlist_1)
        word2 = threading.Thread(target=wordlist_2)
        word3 = threading.Thread(target=wordlist_3)
        word4 = threading.Thread(target=wordlist_4)
        word5 = threading.Thread(target=wordlist_5)
        word6 = threading.Thread(target=wordlist_6)

        word1.start()
        word2.start()
        word3.start()
        word4.start()
        word5.start()
        word6.start()

    except requests.exceptions.ChunkedEncodingError as E:
        pass


def pure_brute_force(): 
    try:
        
        def brute_1():
            while True:
                try:
                    ps = 1
                    nm = "abcdefghijklmnopqrstuvwxyz"
                    nm = "".join(random.sample(nm, ps))
                    dom = "https://"+nm+"."+url

                    string = dom
                    string = str(string)
                    string = string.replace("https://","")
                    string=string.replace("http://","")
                    no_hp_sub = string
                    
                    try:
                        r = requests.get(dom)
                        if dom in list:
                            pass
                        else:
                            if r.status_code == 200:
                                list.append(dom)
                                ip = socket.gethostbyname(no_hp_sub)
                                response = requests.get(f'http://ip-api.com/json/{ip}').content
                                data = json.loads(response)
                                string = f'''{data['isp']}'''
                                string = str(string)
                                if "Cloudflare, Inc." in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                elif "Amazon" in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                else:
                                    print(dom,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)                 
                    except:
                        pass
                except:
                    return
               

        def brute_2():
            while True:
                try:
                    ps = 2
                    nm = "abcdefghijklmnopqrstuvwxyz"
                    nm = "".join(random.sample(nm, ps))
                    dom = "https://"+nm+"."+url

                    string = dom
                    string = str(string)
                    string = string.replace("https://","")
                    string=string.replace("http://","")
                    no_hp_sub = string
                    
                    try:
                        r = requests.get(dom)
                        if dom in list:
                            pass
                        else:
                            if r.status_code == 200:
                                list.append(dom)
                                ip = socket.gethostbyname(no_hp_sub)
                                response = requests.get(f'http://ip-api.com/json/{ip}').content
                                data = json.loads(response)
                                string = f'''{data['isp']}'''
                                string = str(string)
                                if "Cloudflare, Inc." in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                elif "Amazon" in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                else:
                                    print(dom,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)

                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                                    
                    except:
                        pass
                except:
                    return
                            
        def brute_3():
            while True:
                try:
                    ps = 3
                    nm = "abcdefghijklmnopqrstuvwxyz"
                    nm = "".join(random.sample(nm, ps))
                    dom = "https://"+nm+"."+url

                    string = dom
                    string = str(string)
                    string = string.replace("https://","")
                    string=string.replace("http://","")
                    no_hp_sub = string
                    
                    try:
                        r = requests.get(dom)
                        if dom in list:
                            pass
                        else:
                            if r.status_code == 200:
                                list.append(dom)
                                ip = socket.gethostbyname(no_hp_sub)
                                response = requests.get(f'http://ip-api.com/json/{ip}').content
                                data = json.loads(response)
                                string = f'''{data['isp']}'''
                                string = str(string)
                                if "Cloudflare, Inc." in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                elif "Amazon" in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                else:
                                    print(dom,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)            
                    except:
                        pass
                except:
                    return

        def brute_4():
            while True:
                try:
                    ps = 4
                    nm = "1234567890"
                    nm = "".join(random.sample(nm, ps))
                    dom = "https://"+nm+"."+url

                    string = dom
                    string = str(string)
                    string = string.replace("https://","")
                    string=string.replace("http://","")
                    no_hp_sub = string
                    
                    try:
                        r = requests.get(dom)
                        if dom in list:
                            pass
                        else:
                            if r.status_code == 200:
                                list.append(dom)
                                ip = socket.gethostbyname(no_hp_sub)
                                response = requests.get(f'http://ip-api.com/json/{ip}').content
                                data = json.loads(response)
                                string = f'''{data['isp']}'''
                                string = str(string)
                                if "Cloudflare, Inc." in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                elif "Amazon" in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                else:
                                    print(dom,":",ip)
                                    
                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)


                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                    except:
                        pass
                except:
                    return
            
        def brute_num():

            try:

                i = 0
                
                while True:
                    i = i + 1
                    
                    dom = "https://"+str(i)+"."+url

                    string = dom
                    string = str(string)
                    string = string.replace("https://","")
                    string=string.replace("http://","")
                    no_hp_sub = string
                    
                    try:
                        r = requests.get(dom)

                        if dom in list:
                            pass
                        else:
                            if r.status_code == 200:
                                list.append(dom)
                                ip = socket.gethostbyname(no_hp_sub)
                                response = requests.get(f'http://ip-api.com/json/{ip}').content
                                data = json.loads(response)
                                string = f'''{data['isp']}'''
                                string = str(string)
                                if "Cloudflare, Inc." in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Cloudflare"+Fore.WHITE)
                                elif "Amazon" in string:
                                    print(dom,":",ip+Fore.YELLOW+" [WAF] Amazon"+Fore.WHITE)
                                else:
                                    print(dom,":",ip)

                            if r.status_code == 404:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)
                                    print(url_subdomain,":",ip+Fore.RED+" [404]"+Fore.WHITE)

                            if r.status_code == 301:
                                if url_subdomain in list:
                                    pass
                                else:
                                    list.append(url_subdomain)
                                    ip = socket.gethostbyname(no_hp_sub)
                                    response = requests.get(f'http://ip-api.com/json/{ip}').content
                                    data = json.loads(response)
                                    string = f'''{data['isp']}'''
                                    string = str(string)

                                    print(url_subdomain,":",ip+Fore.BLUE+" [301]"+Fore.WHITE)
                                    
                    except:
                        pass
            except:
                return



        brute1 = threading.Thread(target=brute_1)
        brute2 = threading.Thread(target=brute_2)
        brute3 = threading.Thread(target=brute_3)
        brute4 = threading.Thread(target=brute_4)
        brutenum = threading.Thread(target=brute_num)

        brute1.start()
        brute2.start()
        brute3.start()
        brute4.start()
        brutenum.start()

    except requests.exceptions.ChunkedEncodingError as E:
        pass


a1 = threading.Thread(target=wordlists_brute_force)
a2 = threading.Thread(target=pure_brute_force)

print("\n")
a1.start()
time.sleep(0)
a2.start()









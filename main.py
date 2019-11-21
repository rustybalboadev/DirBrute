import random
import requests
import os
import time
from crayons import *
print("""
    ____  _                 
   / __ \(_)____            
  / / / / / ___/            
 / /_/ / / /                
/_______/_/          __     
   / __ )_______  __/ /____ 
  / __  / ___/ / / / __/ _ \\
 / /_/ / /  / /_/ / /_/  __/
/_____/_/   \__,_/\__/\___/ 
                            
""")
file = open('wordlist.txt', 'r')
words = file.read().split("\n")
file.close
url = input("What url do you want to directory bruteforce? (Make sure you have 'https://' and end with '/'!) ")
times = 0 
ExistL = []
dots = ''
while times < len(words):
    url2 = (url + (words[times]))
    request = requests.get(url2)
    if times%20 == 0:
        dots += "\n"
    if request.status_code == 200:
        os.system('cls')
        print("""
        URL: {} exists
        Status Code: {} {}
        """.format(url2, request.status_code, green(".")))
        ExistL.append(url2)
        #time.sleep(1)
        dots += green(" . ")
        print(dots)
        
    else:
        os.system('cls')
        print("""
        URL: {} Doesn't exist
        Status Code: {} {}
        """.format(url2, request.status_code, red(".")))
        dots += red(" . ")
        print(dots)
        #time.sleep(1)

        
    times += 1
choice = input("Do you want to show the url's that exist? ('Yes') ('No') ").lower()
if choice == 'yes':
    for url in ExistL:
        print(url)

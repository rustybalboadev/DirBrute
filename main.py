import requests
import time
import os
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
os.system("cls")
f = open('wordlist.txt', 'r')
words = f.read().split("\n")
f.close()
start = False
times = 0
string = ""
existingURL = []
list500 = []
list409 = []
list404 = []
list403 = []
list400 = []
list204 = []
list201 = []
headers={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "content-type":"text"
}
while start != True:
    url = str(input("What is the url of the website you want to brute? ")).lower()
    if "http://" in url:
        start = True
    elif "https://" in url:
        start = True
    else:
        start = False
        print(red("The URL '{}' doesn't contain http or https.".format(url)))
url2 = url
os.system('cls')
print (green("""
    ____  _                 
   / __ \(_)____            
  / / / / / ___/            
 / /_/ / / /                
/_______/_/          __     
   / __ )_______  __/ /____ 
  / __  / ___/ / / / __/ _ \\
 / /_/ / /  / /_/ / /_/  __/
/_____/_/   \__,_/\__/\___/ 
                            
"""))
print(">" + white("Testing URL: {}".format(url)))
request = requests.get(url2)
print (green(f">>>URL: {url2} Status: {request.status_code}"))
try:
    while times < len(words):
        url2 = (url + (words[times]))
        request = requests.get(url2, headers=headers)
        if request.status_code == 200:
            print("==>" + green("Directory: {} 200 OK".format(url2)))
            existingURL.append(url2)
            #time.sleep(1) you can uncomment this
        elif request.status_code == 500:
            string = (">>>" + red("{} Error: 500 INTERNAL SERVER ERROR".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list500.append(url2)
        elif request.status_code == 409:
            string = (">>>" + red("{} Error: 409 CONFLICT".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list409.append(url2)
        elif request.status_code == 404:
             string = (">>>" + red("{} Error: 404 Not Found".format(url2)))
             print(string)
             #time.sleep(1) you can uncomment this
             list404.append(url2)
        elif request.status_code == 403:
            string = (">>>" + red("{} Error: 403 Forbidden".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list403.append(url2)
        elif request.status_code == 400:
            string = (">>>" + red("{} Error: 400 Bad Request".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list400.append(url2)
        elif request.status_code == 204:
            string = (">>>" + green("{} 204 NO CONTENT".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list204.append(url2)
        elif request.status_code == 201:
            string = (">>>" + green("{} 201 CREATED".format(url2)))
            print(string)
            #time.sleep(1) you can uncomment this
            list201.append(url2)
        times += 1
except KeyboardInterrupt:
    pass

while start == True:
    choice = str(input("What Status codes do you want to print? 500, 409, 404, 403, 400, 204, 201, 200 ('quit' to end): ")).lower()
    if choice == '200':
        print("EXISTING:")
        for url in existingURL:
            print("==> {}".format(green(url)))
    elif choice == '500':
        print("INTERNAL SERVER ERROR:")
        for url in list500:
            print("==> {}".format(red(url)))
    elif choice == '409':
        print("CONFLICT:")
        for url in list409:
            print("==> {}".format(red(url)))
    elif choice == '404':
        print("NOT FOUND:")
        for url in list404:
            print("==> {}".format(red(url)))
    elif choice == '403':
        print("FORBIDDEN:")
        for url in list403:
            print("==> {}".format(red(url)))
    elif choice == '400':
        print("BAD REQUEST:")
        for url in list400:
            print("==> {}".format(red(url)))
    elif choice == '204':
        print("NO CONTENT:")
        for url in list204:
            print("==> {}".format(green(url)))
    elif choice == '201':
        print("CREATED:")
        for url in list201:
            print("==> {}".format(green(url)))
    elif choice == 'quit' or 'q':
        break

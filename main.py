import requests
import os
import argparse
import platform
import time
from crayons import *
from faker import Faker
parser = argparse.ArgumentParser()
fake = Faker()
parser.add_argument('url', help='URL to bruteforce')
parser.add_argument('-w', '--wordlist', help='Define WordList')
parser.add_argument('-t', '--timeout', help='Timeout')
args = parser.parse_args()
print(args.timeout)
if 'http' not in args.url:
    args.url = 'https://{}'.format(args.url)

if args.url[len(args.url)-1:] != '/':
    args.url += '/'
words = []
print(green("""
    ____  _      ____             __     
   / __ \(_)____/ __ )_______  __/ /____ 
  / / / / / ___/ __  / ___/ / / / __/ _ \\
 / /_/ / / /  / /_/ / /  / /_/ / /_/  __/
/_____/_/_/  /_____/_/   \__,_/\__/\___/ 
"""))
def timeout():
    if args.timeout != None:
        time.sleep(int(args.timeout))
f = open(args.wordlist)
for each in f:
    words.append(each.replace('\n', ''))
f.close()
times = 0
print(green("Testing URL: {}\nTotal Words in WList: {}".format(args.url, len(words))))
while times != len(words):
    try:
        req = requests.get(args.url + '{}'.format(words[times]),
                        headers={'User-Agent':fake.user_agent(),
                            'content-type':'text'
                        }
        )
        if req.status_code == 200:
            print(green('-->URL: {}'.format(args.url + '{}'.format(words[times]))))
        else:
            print(red('!>>{} {}'.format(args.url + '{}'.format(words[times]), req.status_code)))
        times += 1
        timeout()
    except KeyboardInterrupt:
        break

    

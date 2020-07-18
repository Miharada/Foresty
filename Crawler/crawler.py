import requests
import argparse
import socket
import json

def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname_ex(host)
        except socket.gaierror:
            ips=[]
        return ips

def writeout(texts):
    f = open(args.o, "a+")
    f.write(texts+"\n")
    f.close()

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('-u', help='Display URL source code', action='store_true')
parser.add_argument('-i', help='Display URL IP Adress', action='store_true')
parser.add_argument('--header', help='Display URL Header',action='store_true')
parser.add_argument('-o', help='Store output to txt file',type=str)

args = parser.parse_args()

response = ""

print(args.url)

if(args.o):
     f = open(args.o, "w+")
     
if(args.u):
    response = requests.get(args.url)
    page_source = response.text
    print("\nURL:", args.url)
    print(page_source)
    if(args.o):
        writeout(page_source)

if(args.i):
    url = args.url.replace('http://','')
    url = args.url.replace('https://','')
    ips = get_ips_for_host(url)
    print(repr(ips))
    if(args.o):
        writeout(repr(ips))
        
if(args.header):
    if(not(args.u)):
        response = requests.get(args.url)
    print(response)
    for i in response.headers:
        print(i,":",response.headers[i])
        if(args.o):
            writeout(texts = i+":"+response.headers[i])
    
    





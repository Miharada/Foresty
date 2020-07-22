import requests
import argparse
import socket
import json
#import nmap

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


def httpremover(url):
    url = args.url.replace('http://','')
    url = args.url.replace('https://','')
    return url
    
def httpadder(url):
    if(url.find('https://') < 0 and url.find('http://') < 0):
        url = 'http://' + url
        print(url)
    return url

def toDict(text):
    if(text):
        text = text.replace('&',':')
        s = text.split(":")
        txtjson = "{"
        i=0
        for j in range(int(len(s)/2)):
            txtjson = txtjson + "\""+ s[i] + "\"" + ":" + "\"" + s[i+1] + "\""
            if(int(len(s)/2)>0):
                txtjson = txtjson + ","
            i+=2
        txtjson = txtjson + "}"
        txtjson = txtjson[:len(txtjson)-2] + "}"
        res = json.loads(txtjson)
        return (res)
    return text

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('-u', help='Display URL source code', action='store_true')
parser.add_argument('-i', help='Display URL IP Adress', action='store_true')
parser.add_argument('--header', help='Display URL Header',action='store_true')
parser.add_argument('-o', help='Store output to txt file',type=str)
parser.add_argument('--ps',help='Port Scan',action='store_true')
parser.add_argument('-H',help='<header/@file> Pass custom header(s) to server', type=str)
parser.add_argument('--data',help='<data> HTTPS POST data', type=str)

args = parser.parse_args()

response = ""


args.url = httpadder(args.url)

print(args.url)
if(args.o):
     f = open(args.o, "w+")
     
if(args.u):
    if(args.H or args.data):
        args.H = toDict(args.H)
        args.data = toDict(args.data)
        response = requests.post(args.url, headers = args.H, data=args.data)
    else:
        response = requests.get(args.url)
    page_source = response.text
    print("\nURL:", args.url)
    print(page_source+"\n")
    if(args.o):
        writeout(page_source+"\n")

if(args.i):
    url = httpremover(args.url)
    ips = get_ips_for_host(url)
    print(repr(ips)+"\n")
    if(args.o):
        writeout(repr(ips)+"\n")

if(args.header):
    if(not(args.u)):
        response = requests.get(args.url)
    print(response)
    for i in response.headers:
        print(i,":",response.headers[i])
        if(args.o):
            writeout(texts = i+":"+response.headers[i])

# if(args.ps):
   
#     ips = socket.gethostbyname(httpremover(args.url))
#     scanner = nmap.PortScanner()
#     for port in range(100):
#         res = scanner.scan(ips,str(port))
#         res = res['scan'][ips]['tcp'][port]['state']
#         print(f'port {port} is {res}.')

#https://stackoverflow.com/questions/52170913/python-nmap-scanner-progress
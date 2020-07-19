import requests
import argparse
import socket
import nmap

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

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('-u', help='Display URL source code', action='store_true')
parser.add_argument('-i', help='Display URL IP Adress', action='store_true')
parser.add_argument('--header', help='Display URL Header',action='store_true')
parser.add_argument('-o', help='Store output to txt file',type=str)
parser.add_argument('--ps',help='Port Scan',action='store_true')

args = parser.parse_args()

response = ""

print(args.url)

if(args.o):
     f = open(args.o, "w+")
     
if(args.u):
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

if(args.ps):
    ips = socket.gethostbyname(httpremover(args.url))
    scanner = nmap.PortScanner()
    for port in range(100):
        print("a")
        res = scanner.scan(ips,str(port))
        res = res['scan'][ips]['tcp'][port]['state']
        print(f'port {port} is {res}.')

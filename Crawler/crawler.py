import requests
import argparse
import socket

def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname_ex(host)
        except socket.gaierror:
            ips=[]
        return ips

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('-u', help='Display URL source code', action='store_true')
parser.add_argument('-i', help='Display URL IP Adress', action='store_true')


args = parser.parse_args()

print(args.url)
if(args.u):
    r = requests.get(args.url)
    page_source = r.text
    print("\nURL:", args.url)
    print(page_source)
if(args.i):
    url = args.url.replace('http://','')
    url = args.url.replace('https://','')
    ips = get_ips_for_host(url)
    print(repr(ips))



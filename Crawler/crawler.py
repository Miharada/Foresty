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
parser.add_argument('-u', help='Display URL source code', type=str)
parser.add_argument('-i', help='Display URL IP Adress', action='store_true')

args = parser.parse_args()

if(args.u):
    r = requests.get(args.u)
    page_source = r.text
    print("\nURL:", args.u)
    print(page_source)
if(args.i):
    url = args.u.replace('http://','')
    url = args.u.replace('https://','')
    ips = get_ips_for_host(url)
    print(repr(ips))



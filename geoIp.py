from pwn import *
import requests, argparse, time

parser=argparse.ArgumentParser('IP Geolocation')
parser.add_argument('-ip', '--target',required=True ,help='Specify IP or Domain Name')
args=parser.parse_args()

target = args.target

URL='http://ip-api.com/json/'

def ip_geo(URL):
    
    r = requests.get(URL + target).json()
    print('\n')

    p1 = log.progress(f" Locating IP - {target} ...")
    time.sleep(2)

    print('\n' + '      - Country:    ' + r.get('country') + '\n' + '      - RegionName: ' + r.get('regionName') + '\n' + '      - City:       ' + r.get('city'))
   
    print('      - Latitude:  ', r.get('lat'))
    print('      - Longitude: ', r.get('lon'))

if __name__=='__main__':
    ip_geo(URL)

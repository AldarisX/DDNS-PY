import socket
import requests
from config import Config


def get_ip():
    if(Config().get_use_loc_ip()):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
    else:
        hreq = requests.get("http://icanhazip.com/")
        ip = hreq.text.replace("\n", "")
    print("Your IP is "+ip)
    return ip

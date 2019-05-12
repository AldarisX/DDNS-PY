import socket
import requests
from config import Config


def get_ip():
    ip = "-1"
    if(Config().get_use_loc_ip()):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
        except Exception as err:
            print("获取IP失败")
    else:
        try:
            hreq = requests.get("http://icanhazip.com/")
            ip = hreq.text.replace("\n", "")
        except Exception as err:
            print("获取IP失败")
    print("Your IP is "+ip)
    if(ip == "-1"):
        return get_ip()

    return ip

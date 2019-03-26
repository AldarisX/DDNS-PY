import json
import time
from util import ip
from util import record
from config import Config

def ctrol():
    rip = ip.get_ip()

    # 要求的域名，将DomainName作为key
    domainDict = {}
    # 读取配置文件
    dnList = Config().get_record()
    for i, dn in enumerate(dnList):
        if(dn["DomainName"] in domainDict):
            dn["isPass"] = False
            domainDict[dn["DomainName"]].update(dn)
        else:
            dn["isPass"] = False
            records = {dn["DomainName"]: [dn]}
            domainDict.update(records)

    # 遍历配置文件中的域名
    for i, domain in enumerate(domainDict):
        # 获取这个域名的注册记录
        domainList = record.query_record(domain)
        # 遍历已经注册的记录
        for j, rdn in enumerate(domainList):
            # 按域名遍历配置文件中的域名
            for k, recordDomain in enumerate(domainDict[rdn["DomainName"]]):
                # 如果RR值跟配置的RR匹配
                if(rdn["RR"] == recordDomain["RR"]):
                    # 如果IP不匹配
                    if (not rdn["Value"] == rip):
                        # 按照排序 最新的记录在第一个 所以isPass=false
                        if (not recordDomain["isPass"]):
                            rdn["Value"] = rip
                            record.update_record(rdn)
                            print("UPDATE: " + rdn["RR"]+"." +
                                  rdn["DomainName"]+" "+rdn["Value"])
                            recordDomain["isPass"] = True
                        else:
                            record.delete_record(rdn)
                            print("DELETE: " + rdn["RR"]+"." +
                                  rdn["DomainName"]+" "+rdn["Value"])
                    else:
                        recordDomain["isPass"] = True
    # 如果没有注册
    for i, domain in enumerate(domainDict):
        for j, wdn in enumerate(domainDict[domain]):
            if(not wdn["isPass"]):
                wdn["Value"] = rip
                record.add_record(wdn)
                print("ADD: " + wdn["RR"]+"." +
                      wdn["DomainName"]+" "+wdn["Value"])

if(Config().get_loop()):
    while(Config().get_loop()):
        ctrol()
        time.sleep(Config().get_sleep_time())
else:
    ctrol()
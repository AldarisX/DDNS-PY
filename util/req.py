from config import Config
from aliyunsdkcore.request import CommonRequest

def get_req():
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type(Config().get_protocol_type())  # https | http
    request.set_version('2015-01-09')
    return request

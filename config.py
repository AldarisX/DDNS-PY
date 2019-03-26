import json
from aliyunsdkcore.client import AcsClient


class Config:
    def __init__(self):
        f = open("config.json")
        setting = json.load(f)
        self.set_access_key_id(setting["accessKeyId"])
        self.set_secret(setting["secret"])
        self.set_use_loc_ip(setting["useLocIp"])
        self.set_protocol_type(setting["protocolType"])
        self.set_sleep_time(setting["sleepTime"])
        self.set_loop(setting["loop"])
        self.set_record(setting["record"])

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Config, cls)
            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance

    def get_client(self):
        return AcsClient(
            self.get_access_key_id(),
            self.get_secret(),
            'cn-hangzhou'
        )

    def get_access_key_id(self):
        return self.access_key_id

    def set_access_key_id(self, access_key_id):
        self.access_key_id = access_key_id

    def get_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret

    def get_use_loc_ip(self):
        return self.use_loc_ip

    def set_use_loc_ip(self, use_loc_ip):
        self.use_loc_ip = use_loc_ip

    def get_protocol_type(self):
        return self.protocol_type

    def set_protocol_type(self, protocol_type):
        self.protocol_type = protocol_type

    def get_sleep_time(self):
        return self.sleep_time

    def set_sleep_time(self, sleep_time):
        self.sleep_time = sleep_time

    def get_loop(self):
        return self.loop

    def set_loop(self, loop):
        self.loop = loop

    def get_record(self):
        return self.record

    def set_record(self, record):
        self.record = record

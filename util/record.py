import json
from . import req
from config import Config

def add_record(record):
    request = req.get_req()
    request.set_action_name('AddDomainRecord')

    request.add_query_param('DomainName', record['DomainName'])
    request.add_query_param('RR', record['RR'])
    request.add_query_param('Type', record['Type'])
    request.add_query_param('Value', record['Value'])

    response = Config().get_client().do_action_with_exception(request)

    result = json.loads(response)
    return result

def delete_record(record):
    request = req.get_req()
    request.set_action_name('AddDomainRecord')

    request.add_query_param('RecordId', record['RecordId'])

    response = Config().get_client().do_action_with_exception(request)

    result = json.loads(response)
    return result

def update_record(record):
    request = req.get_req()
    request.set_action_name('UpdateDomainRecord')

    request.add_query_param('RecordId', record["RecordId"])
    request.add_query_param('RR', record["RR"])
    request.add_query_param('Type', record['Type'])
    request.add_query_param('Value', record['Value'])

    response = Config().get_client().do_action_with_exception(request)

    result = json.loads(response)
    return result

def query_record(domainName):
    request = req.get_req()
    request.set_action_name('DescribeDomainRecords')

    request.add_query_param('DomainName', domainName)

    response = Config().get_client().do_action_with_exception(request)

    result = json.loads(response)
    return result["DomainRecords"]["Record"]
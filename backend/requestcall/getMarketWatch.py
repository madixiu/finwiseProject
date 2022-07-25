import requests
import json
from .util.Convereter_trunc import truncater
from .util.dataAlterTest import numberGen

# def getMarketWatchRequest(name,industry):
#     # try:
#     resp = requests.get('http://185.231.115.223:3000/ViewWatch')
#     if resp.status_code == 200:
#         if resp.text:
#             js = json.loads(resp.text)
#             js = additionalDataMarketWatch(js)
#             if (name != None or industry != None):
#                 filtered = getFilteredData(name,industry,js)
#                 return filtered
#             else:
#                 return js
                
def getMarketWatchRequest():
    resp = requests.get('http://185.231.115.223:3000/ViewWatch')
    if resp.status_code == 200:
        if resp.text:
            js = json.loads(resp.text)
            js = additionalDataMarketWatch(js)
            return js





def additionalDataMarketWatch(input):
    for item in input:
        
        # item["number"] = numberGen()
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None
    return sorted(input, key=lambda x: x['ticker'],reverse=False)

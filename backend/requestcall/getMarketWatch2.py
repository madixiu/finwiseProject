import requests
import json
from .util.Convereter_trunc import truncater

def getMarketWatchRequest(name,industry):
    # try:
    resp = requests.get('http://185.231.115.223:3000/ViewWatch')
    if resp.status_code == 200:
        if resp.text:
            js = json.loads(resp.text)
            additionalDataMarketWatch(js)
            if (name != None or industry != None):
                filtered = getFilteredData(name,industry,js)
                return filtered
            else:
                return js
def getMarketWatchRequest():
    resp = requests.get('http://185.231.115.223:3000/ViewWatch')
    if resp.status_code == 200:
        if resp.text:
            js = json.loads(resp.text)
            additionalDataMarketWatch(js)
            return js


def getMarketWatchFilterLists():
    filters=[]
    input = getMarketWatchRequest()
    for item in input:
        if item["industry"] not in filters  and item["industry"] != None:
            filters.append(item["industry"])
    return filters

def additionalDataMarketWatch(input):
    for item in input:
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None


def getFilteredData(marketName,marketIndustry):
    dataTemp=[]
    # print(marketName)
    # print(marketIndustry)
    input = getMarketWatchRequest()

    # print(input)
    if marketIndustry == []:
        if marketName =='همه':
            return input
        elif marketName == 'بورس':
            dataTemp = [x for x in input if x["marketParent"] == 1]
            return dataTemp
        elif marketName == "فرابورس":
            dataTemp = [x for x in input if (x["marketParent"] == 2 or x["marketParent"] == 20)]
            return dataTemp
    else:
        if marketName =='همه':
            dataTemp=[]
            dataTemp = [x for x in input if (x["industry"] in marketIndustry)]

            return dataTemp
        elif marketName == "بورس":
            dataTemp = [x for x in input if (x["marketParent"] == 1 and x["industry"] in marketIndustry)]
            return dataTemp
        elif marketName == "فرابورس":
            dataTemp = [x for x in input if (x["marketParent"] == 2 or x["marketParent"] == 20) and x["industry"] in marketIndustry]
            return dataTemp
import json
from django.http.response import JsonResponse
import requests

def ListOfStocks():
    resp = requests.get("http://185.231.115.223:3000/View_TV_List")
    if resp.status_code == 200:
        js = json.loads(resp.text)
        dict = ListOfStockNames(js)
        restructData(js)
        result = [dict,js]
        # print(js)
        return (result)
    else:
        return ("NoData")


def TVtickerData(limits,url,todate):
    payload = {'limits': limits, 'url': url,'todate': todate}
    resp = requests.get("http://185.231.115.223:3000/rpc/ViewTVDaily",payload)
    if resp.status_code == 200:
        return json.loads(resp.text)

def ListOfStockNames(js):
    dict={}
    for item in js:
        dict[item["symbol"]]=item["ExchangeType"]
    return dict
    # print(len(js))
    # print(dict)
def restructData(input):
    for item in input:
        if item["ExchangeType"] == "سهم بورس":
            item["exchange"] = "بورس"
        elif item["ExchangeType"] == "سهم فرابورس":
            item["exchange"] = "فرابورس"
        item["type"] = "سهام"
        item.pop("ExchangeType",None)
        item["urlparam"] = item.pop("urlParameter")
    # print(input)

        
    
# ListOfStocks()


import json
import requests

def ListOfStocks():
    resp = requests.get("http://37.152.180.99:3000/View_TV_List")
    if resp.status_code == 200:
        js = json.loads(resp.text)
        ListOfStockNames(js)
        return (json.loads(resp.text))
    else:
        return ("NoData")

def ListOfStockNames(js):
    print("*******************************************")
    for item in js:
        print("\""+item["symbol"]+"\""+':'+"\""+item["ExchangeType"]+"\""+",")
            # item["symbol"]+":"+item["ExchangeType"])
    print(len(js))
        
    
# ListOfStocks()


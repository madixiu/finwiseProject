import requests
import json
from .util.Convereter_trunc import truncater
def getMapData():
    resp = requests.get("http://37.152.180.99:3000/View_TreeMapInitial")
    if resp.status_code == 200:
        js = json.loads(resp.text)
        temp = js[0]["industry"]
        TempMarketCap = 0
        final = []
        child = []
        industryList =[]
        for item in js:
            if not item["industry"] in industryList:
                industryList.append(item["industry"])
        for item in js:
            if (item["industry"] == temp):
                TempMarketCap+=item["MarketCap"]
                child.append({"id":item["ID"], "name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})
                if item["industry"] == industryList[-1] and item == js[-1]:
                    final.append({"name": temp, "children": child})

            elif item["industry"] != temp and item["industry"] != industryList[-1]:
                final.append({"name": temp, "children": child })
                TempMarketCap = item["MarketCap"]
                temp = item["industry"]
                child=[]
                child.append({"id":item["ID"],"name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})
            elif item["industry"] != temp and item["industry"] == industryList[-1]:
                final.append({"name": temp, "children": child })
                TempMarketCap = item["MarketCap"]   
                temp = item["industry"]
                child=[]
                child.append({"id":item["ID"],"name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})

        mapDataObj = {"name":"MAP", "children":final}
        # print(mapDataObj)
        return mapDataObj
    # print("hi")

# getMapData()
    # temp = js[0]["industry"]
    # TempMarketCap = 0
    # final = []
    # child = []
    # industryList =[]

    # for item in js:
    #     if not item["industry"] in industryList:
    #         industryList.append(item["industry"])
    # for item in js:
    #     if (item["industry"] == temp):
    #         TempMarketCap+=item["MarketCap"]
    #         child.append({"name": item["ticker"],"value": item["MarketCap"]})
    #         if item["industry"] == industryList[-1] and item == js[-1]:
    #             final.append({"name": temp, "children": child ,"value": TempMarketCap})

    #     elif item["industry"] != temp and item["industry"] != industryList[-1]:
    #         final.append({"name": temp, "children": child ,"value": TempMarketCap})
    #         TempMarketCap = item["MarketCap"]
    #         temp = item["industry"]
    #         child=[]
    #         child.append({"name": item["ticker"],"value": item["MarketCap"]})
    #     elif item["industry"] != temp and item["industry"] == industryList[-1]:
    #         final.append({"name": temp, "children": child ,"value": TempMarketCap})
    #         TempMarketCap = item["MarketCap"]
    #         temp = item["industry"]
    #         child=[]
    #         child.append({"name": item["ticker"],"value": item["MarketCap"]})

    # mapDataObj = {"children":[{"name": "بورس ایران", "children":final}]}

    # prices={}
    # k={}
    # for item in js:
    #     j={}
    #     j['p']=item['p']
    #     # print(item['cp'])
    #     if item['cp'] != None:
    #         j['cp']=truncater(item['cp'])
    #     k[item['ticker']]=j
    # prices['errCode']=0
    # prices['msg']=''
    # prices['data']=k

    # result = {"mapDataObj":mapDataObj,"prices":prices}
    # return result

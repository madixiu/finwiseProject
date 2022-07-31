import requests
import json
from requestcall.util.Convereter_trunc import truncater
def getMapData():
    try:
        resp = requests.get("http://185.231.115.223:3000/View_TreeMapInitial")
        if resp.status_code == 200 and resp.text != [] or resp.text != None:
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
                if item["industry"] == temp:
                    if item["MarketCap"] != None:

                        TempMarketCap+=item["MarketCap"]
                        child.append({"id":item["ID"], "name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})
                        if item["industry"] == industryList[-1] and item == js[-1]:
                            final.append({"name": temp, "children": child})

                elif item["industry"] != temp and item["industry"] != industryList[-1]:
                    if item["MarketCap"] != None:

                        final.append({"name": temp, "children": child })
                        TempMarketCap = item["MarketCap"]
                        temp = item["industry"]
                        child=[]
                        child.append({"id":item["ID"],"name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})
                elif item["industry"] != temp and item["industry"] == industryList[-1]:
                    if item["MarketCap"] != None:

                        final.append({"name": temp, "children": child })
                        TempMarketCap = item["MarketCap"]   
                        temp = item["industry"]
                        child=[]
                        child.append({"id":item["ID"],"name": item["ticker"],"close":item["p"],"change":truncater(item["cp"]),"value": item["MarketCap"],"tickerFull": item["tickerFull"]})

            mapDataObj = {"name":"نقشه بازار", "children":final}
        
            return mapDataObj
    except:
        return "noData"
    return "noData"
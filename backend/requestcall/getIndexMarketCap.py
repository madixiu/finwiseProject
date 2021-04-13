import requests
import json

def IndexMarketCapRequest():
    resp = requests.get('http://37.152.180.99:3000/View_IndexMarketCap')
    if resp.status_code == 200:
        js = json.loads(resp.text)
        result = dataAlter(js)
        
        return (result)
    else:
        return("noData")

def dataAlter(input):
    Sorted = []
    Others = []
    marketCapOthers = 0
    input = sorted(input, key=lambda x : x['marketCap'], reverse=True)
    
    for i,item in enumerate(input):
        if (i < 9):
            Sorted.append(item)
        else:
            marketCapOthers = item["marketCap"] + marketCapOthers
            Others.append(item)

    result = [{"TopIndustries":Sorted},{"Others":{"marketCapSum":marketCapOthers,"List":Others}}]
    return result

# IndexMarketCapRequest()


import requests
import json

def SearchData():
    try:
        resp = requests.get('http://185.231.115.223:3000/View_SearchBar')
        if resp.status_code == 200:
            MainData = json.loads(resp.text)
            return MainData
    except:
            "noData"
    # try:
    #     resp2 = requests.get('http://162.55.15.105:3000/View_Search')
    #     if resp2.status_code == 200:
    #         additionalData = json.loads(resp2.text)

    # except:
    #     additionalData = []
    
    return "noData"


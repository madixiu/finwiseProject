import requests
import json

def SearchData():
    try:
        resp = requests.get('http://185.231.115.223:3000/View_SearchBar')
        if resp.status_code == 200:
            data = json.loads(resp.text)
            return data
    except:
           return "noData" 
    return "noData"


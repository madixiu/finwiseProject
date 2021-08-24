import requests
import json

def SearchData():
    resp = requests.get('http://185.231.115.223:3000/View_SearchBar')
    resp2 = requests.get('http://162.55.15.105:3000/View_Search')
    if resp.status_code == 200 or resp2.status_code==200:
        # return (json.loads('['+resp.text[1:-1]+', \n '+resp2.text[1:-1]+']'))
        return (json.loads(resp.text)+json.loads(resp2.text))
    else:
        return ("noData")

import requests
import json

def SearchData():
    resp = requests.get('http://185.231.115.223:3000/View_SearchBar')
    if resp.status_code == 200:
        return (json.loads(resp.text))
    else:
        return ("noData")
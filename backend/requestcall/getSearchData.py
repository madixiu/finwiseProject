import requests
import json

def SearchData():
    resp = requests.get('http://37.152.180.99:3000/View_SearchBar')
    if resp.status_code == 200:
        return (json.loads(resp.text))
    else:
        return ("noData")
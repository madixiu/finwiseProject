import json
import requests

def ListOfStocks():
    resp = requests.get("http://37.152.180.99:3000/View_TV_List")
    if resp.status_code == 200:
        return (json.loads(resp.text))
    else:
        return ("NoData")


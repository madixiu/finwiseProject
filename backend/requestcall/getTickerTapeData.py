import requests
import json

def TickerTapeData():
    resp = requests.get('http://37.152.180.99:3000/View_Marquee')
    if resp.status_code == 200:
        print(resp.text)
        return (json.loads(resp.text))

    else:
        return("noData")
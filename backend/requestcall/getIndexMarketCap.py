import requests
import json

def IndexMarketCapRequest():
    resp = requests.get('http://37.152.180.99:3000/View_IndexMarketCap')
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")
import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
def getbasicCommodity():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'commodity'}
        resp = requests.get('http://162.55.15.105:3000/View_Basic_IRComm',headers=head)
        if resp.status_code == 200:
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")

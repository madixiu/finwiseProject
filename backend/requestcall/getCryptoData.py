import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
def getCryptoTechnicalIndicators():
    ct=0
    while ct<3:
        resp = requests.get('http://45.147.77.195:3000/View_Crypto_Indicators')
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
def getCryptoCorrelation():
    ct=0
    while ct<3:
        resp = requests.get('http://45.147.77.195:3000/View_Crypto_Corr')
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
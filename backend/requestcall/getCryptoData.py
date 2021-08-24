import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
def getCryptoTechnicalIndicators():
    ct=0
    while ct<3:
        resp = requests.get('http://162.55.15.105:3000/View_Crypto_Indicators')
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")


# def getSingleCryptoLive(firm):
#     ct=0
#     while ct<3:
#         url='https://coin360.com/api/coins/card?currency=USD&coin='+str(firm)
#         print(url)
#         resp = requests.get(url)
#         if resp.status_code == 200:
    
#             # return(resp.text)
#             return (json.loads(resp.text))
#             # return(json.loads(resp.text))
#         else:
#             time.sleep(2)
#             ct=ct+1
#     return ("noData")
# def getBasicCryptoData(firm):
#     ct=0
#     while ct<3:
#         resp = requests.get('http://162.55.15.105:3000/View_BasicSingleCrypto?"ID"=eq.'+str(firm))
#         if resp.status_code == 200:
    
#             # return(resp.text)
#             return (json.loads(resp.text))
#             # return(json.loads(resp.text))
#         else:
#             time.sleep(2)
#             ct=ct+1
#     return ("noData")

def getCryptoCorrelation():
    ct=0
    while ct<3:
        resp = requests.get('http://162.55.15.105:3000/View_Crypto_Corr')
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")


def getBCMarketWatch():
    ct=0
    while ct<3:
        resp = requests.get('http://162.55.15.105:3000/View_Crypto_MarketWatch')
        if resp.status_code == 200:
            js = json.loads(resp.text)
            for index,item in enumerate(js):
                item["id"] = index
            return (js)
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
def getBCMarketWatchAll():
    ct=0
    while ct<3:
        resp = requests.get('http://162.55.15.105:3000/View_Crypto_MarketWatch_All')
        if resp.status_code == 200:
            js = json.loads(resp.text)
            for index,item in enumerate(js):
               item["id"] = index
            return (js)
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
def getSingleCryptoTechnical(firm):
     ct=0
     while ct<3:
        resp = requests.get('http://162.55.15.105:3000/View_Crypto_Indicator?coin1=eq.'+str(firm))
        if resp.status_code == 200:
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1  
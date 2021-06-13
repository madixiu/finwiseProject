import requests
import json 
import pandas as pd
from khayyam import *
from datetime import datetime
from .util.Convereter_trunc import truncater

def getOraghData():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_Watch_Bonds',headers = head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        js = additionalData(js)
        return js
    else:
        return ("noData")

def getHaghTaghadomData(): 
    resp = requests.get('http://185.231.115.223:3000/View_Watch_HaghTaghadoms')
    if resp.status_code == 200:
        js = json.loads(resp.text)
        TaghadomDataFix(js)
        return js
    else:
        return ("noData")

def getFundsData():
    resp = requests.get('http://185.231.115.223:3000/View_Watch_ETF')
    if resp.status_code == 200:
        js = json.loads(resp.text)
        js = additionalData(js)
        return js
    else:
        return ("noData")

def additionalData(data):
    for item in data:
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None
    data = sorted(data, key=lambda x : x["ticker"],reverse=False)
    return data

def TaghadomDataFix(data):
    for item in data:
        item['Coverage'] = truncater(item['Coverage'])
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None

def getCryptoMarketData():

    head = {'Accept-Profile':'crypto'}
    resp = requests.get('http://162.55.15.105:3000/View_Crypto',headers=head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        DF=pd.DataFrame(js)
        # DF=pd.read_json(js)
        # print(DF.head())
        DF['persianDate']=DF['regularMarketTime'].apply(lambda x:str(JalaliDatetime(datetime.fromtimestamp(x))))
        # return(json.loads(pd.DataFrame.to_json(DF,orient="index")))
        return DF.to_dict('records')

    else:
        return ("noData")
import requests
import json
import pandas as pd
# from .util.Convereter_trunc import truncater, converter
import time
def getbasicCommodityIR():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'commodity'}
        resp = requests.get('http://162.55.15.105:3000/View_live_IR',headers=head)
        if resp.status_code == 200:
            # return (json.loads(resp.text))
            DX=pd.DataFrame(json.loads(resp.text))
            DX['Date']=DX['engDate']+' '+DX['persianD']
            DX['Date']=DX['Date'].apply(lambda x: x.split(' ')[2]+' '+x.split(' ')[1] if  len(x.split(' '))>2 else x.split(' ')[1])
            ll=[ 'گرم ۱۸ عیار',
            'گرم ۲۴ عیار',
            'طلای آبشده معامله',
            'دلار نیما-خرید',
            'دلار نیما-فروش',
            'دلار لحظه ای',
            'دلار بازار',
            'یورو',
            'دلار سنا-خرید',
            'دلار سنا-فروش',
            'سکه بهار آزادی',
            'سکه امامی']
            DX1=DX[DX['persianName'].isin(ll)]
            DX1=DX1[['persianName','category','price','d','dp','Date']]
            DX1.sort_values(by=['category','persianName'],inplace=True)
            DX=DX[['persianName','category','price','d','dp','Date']]
            DX2=DX[DX['category']=='Gold']
            DX3=DX[DX['category']=='Currency']
            return {1:json.loads(DX1.to_json(orient='records')),2:json.loads(DX2.to_json(orient='records')),3:json.loads(DX3.to_json(orient='records'))}
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
def getbasicInvesting():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'commodity'}
        resp = requests.get('http://162.55.15.105:3000/View_Investing_Live',headers=head)
        if resp.status_code == 200:
            DX=pd.DataFrame(json.loads(resp.text))
            DX['persianDate']=DX['persianDate'].apply(lambda x:str(x).replace('.000000',''))
            DX2=DX[DX['Type']=='Metal']
            DX3=DX[DX['Type']=='Energy']
            DX4=DX[DX['Type']=='Currencies']
            return {1:json.loads(DX2.to_json(orient='records')),2:json.loads(DX3.to_json(orient='records')),3:json.loads(DX4.to_json(orient='records'))}
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")

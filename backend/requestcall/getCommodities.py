import requests
import json
import datetime
import pandas as pd
# from .util.Convereter_trunc import truncater, converter
import time


def getbasicCommodityIR():
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'commodity'}
        resp = requests.get(
            'http://162.55.15.105:3000/View_live_IR', headers=head)
        if resp.status_code == 200:
            # return (json.loads(resp.text))
            DX = pd.DataFrame(json.loads(resp.text))
            DX['Date'] = DX['engDate']+' '+DX['persianD']
            DX['Date'] = DX['Date'].apply(lambda x: x.split(
                ' ')[2]+' '+x.split(' ')[1] if len(x.split(' ')) > 2 else x.split(' ')[1])
            ll = ['گرم ۱۸ عیار',
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
            DX1 = DX[DX['persianName'].isin(ll)]
            DX1 = DX1[['persianName', 'category',
                       'price', 'd', 'dp', 'Date', 'ID']]
            DX1.sort_values(by=['category', 'persianName'], inplace=True)
            DX = DX[['persianName', 'category',
                     'price', 'd', 'dp', 'Date', 'ID']]
            DX2 = DX[DX['category'] == 'Gold']
            DX3 = DX[DX['category'] == 'Currency']
            return {1: json.loads(DX1.to_json(orient='records')), 2: json.loads(DX2.to_json(orient='records')), 3: json.loads(DX3.to_json(orient='records'))}
        else:
            time.sleep(2)
            ct = ct+1
    return "noData"


def getbasicInvesting():
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'commodity'}
        resp = requests.get(
            'http://162.55.15.105:3000/View_Investing_Live', headers=head)
        if resp.status_code == 200:
            DX = pd.DataFrame(json.loads(resp.text))
            DX['persianDate'] = DX['persianDate'].apply(
                lambda x: str(x).replace('.000000', ''))
            DX['changeperc'] = DX['changeperc'].apply(
                lambda x: float(str(x).replace('%', '').replace('+', '')))
            DX2 = DX[DX['Type'] == 'Metal']
            DX3 = DX[DX['Type'] == 'Energy']
            DX4 = DX[DX['Type'] == 'Currencies']
            DX5 = DX[DX['Type'] == 'Indices']
            return {1: json.loads(DX2.to_json(orient='records')), 2: json.loads(DX3.to_json(orient='records')), 3: json.loads(DX4.to_json(orient='records')), 4: json.loads(DX5.to_json(orient='records'))}
        else:
            time.sleep(2)
            ct = ct+1
    return "noData"


def getPetroCommodity():
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'commodity'}
        resp = requests.get(
            'http://162.55.15.105:3000/View_Live_Petro', headers=head)
        if resp.status_code == 200:
            js = json.loads(resp.text)
            for item in js:
                if item["price"] == "NaN":
                    item["price"] = "-"

            return js
        else:
            time.sleep(2)
            ct = ct+1
    return "noData"


def getMBcommodity():
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'commodity'}
        resp = requests.get(
            'http://162.55.15.105:3000/View_MB_Live', headers=head)

        if resp.status_code == 200:
            js = json.loads(resp.text)
            for item in js:
                year = item["persianDate"][:4]
                month = item["persianDate"][4:6]
                day = item["persianDate"][6:8]
                item["persianDate"] = year + '-'+month+'-'+day
            return js
        else:
            time.sleep(2)
            ct = ct+1
    return "noData"


def unixConvertor(timestamp):
    if len(timestamp) > 10:
        timestamp = timestamp.split(' ')
        # timestamp = timestamp[0].split('-')
        timestamp = [timestamp[:4], timestamp[5:7], timestamp[8:10]]
    else:
        # timestamp= timestamp.split('/')
        timestamp = [timestamp[:4], timestamp[5:7], timestamp[8:10]]

    return int(datetime.datetime(int(timestamp[0]), int(timestamp[1]), int(timestamp[2]), 0, 0, 0).strftime('%s'))*1000
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DETAIL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def getHistoricIR(identifier):
    head = {'Accept-Profile': 'commodity'}
    resp = requests.get(
        'http://162.55.15.105:3000/View_Historic_IR?ID=eq.' + str(identifier), headers=head)

    if resp.status_code == 200:
        # js = json.loads(resp.text)
        DX = pd.DataFrame(json.loads(resp.text))
        # DX['unix']=DX['timestamp'].apply(unixConvertor)
        DX = DX[DX['persianDate'].str.contains('/')]
        DX = DX[['ID', 'persianName', 'price', 'high', 'low',
                 'd', 'dp', 'timestamp', 'persianDate', 'open']]
        DX['persianDate'] = DX['persianDate'].apply(lambda x: x.split(' ')[0])
        DX["iid"] = DX.index
        j1 = json.loads(DX.to_json(orient='records'))
        DX.sort_values(by=['timestamp'], ascending=True, inplace=True)
        p = DX['price'].tolist()
        d = DX['persianDate'].tolist()
        # u=DX['unix'].tolist()
        S = {"series": p, "categories": d}
        return {'chart': S, 'table': j1}
    else:
        return "noData"


def getHistoricInvesting(identifier):
    head = {'Accept-Profile': 'commodity'}
    resp = requests.get(
        'http://162.55.15.105:3000/View_Historic_Investing?pairID=eq.' + str(identifier), headers=head)

    if resp.status_code == 200:
        # js = json.loads(resp.text)
        DX = pd.DataFrame(json.loads(resp.text))
        # DX['unix']=DX['UTC']*1000
        # DX=DX[DX['persianDate'].str.contains('/')]
        DX = DX[['pairID', 'persianName', 'Close', 'High',
                 'Low', 'Open', 'Volume', 'engDate', 'persianDate']]
        # DX['persianDate']=DX['persianDate'].apply(lambda x: x.split(' ')[0])
        DX["iid"] = DX.index
        j1 = json.loads(DX.to_json(orient='records'))
        DX.sort_values(by=['engDate'], ascending=True, inplace=True)
        p = DX['Close'].tolist()
        d = DX['persianDate'].tolist()
        # u=DX['unix'].tolist()
        S = {"series": p, "categories": d}
        return {'chart': S, 'table': j1}
        # return js
    else:
        return "noData"


def getHistoricPlats(identifier):
    head = {'Accept-Profile': 'commodity'}
    resp = requests.get(
        'http://162.55.15.105:3000/View_Historic_Plats?ID=eq.' + str(identifier), headers=head)

    if resp.status_code == 200:
        # js = json.loads(resp.text)
        DX = pd.DataFrame(json.loads(resp.text))
        # DX['unix']=DX['UTC']*1000
        # DX=DX[DX['persianDate'].str.contains('/')]
        DX.sort_values(by=['engdate'], ascending=False, inplace=True)
        DX = DX[['ID', 'persianName', 'persianCategory', 'unit',
                 'price', 'engdate', 'persianDate', 'location']]
        DX['persianDate'] = DX['persianDate'].apply(lambda x: x.split(' ')[0])
        DX["iid"] = DX.index
        j1 = json.loads(DX.to_json(orient='records'))
        DX.sort_values(by=['engdate'], ascending=True, inplace=True)
        p = DX['price'].tolist()
        d = DX['persianDate'].tolist()
        # u=DX['unix'].tolist()
        S = {"series": p, "categories": d}
        return {'chart': S, 'table': j1}
        # return js
    else:
        return "noData"

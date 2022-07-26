
import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
import pandas as pd


def getFundsIndustryComposition(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'funds'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/latestindustrycomp?a='+identifier, headers=head)
        if resp.status_code == 200:
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct = ct+1

    return "noData"


def getFundsAssetComposition(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'funds'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/latest_asset_typecomp?a='+identifier, headers=head)
        if resp.status_code == 200:
            DX = pd.DataFrame(json.loads(resp.text))
            DX.replace('OtherAssetTodayPercent',
                       'سایر دارایی ها', inplace=True)
            DX.replace('DepositTodayPercent', 'سپرده', inplace=True)
            DX.replace('BondTodayPercent', 'اوراق با درآمد ثابت', inplace=True)
            DX.replace('CashTodayPercent', 'وجه نقد', inplace=True)
            DX.replace('TopFiveStockTodayPercent',
                       'پنج سهم اصلی', inplace=True)
            return (json.loads(DX.to_json(orient='records')))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct = ct+1

    return "noData"


def getFundsLive(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'funds'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/live_fund?a='+identifier, headers=head)
        if resp.status_code == 200:

            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct = ct+1

    return "noData"


def getFundsHistoricalNavData(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'funds'}
        resp = requests.get(
            'http://185.231.115.223:3000/View_HistoricNAV?FundID=eq.'+str(identifier), headers=head)
        if resp.status_code == 200:

            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct = ct+1

    return "noData"


def getFundsMetaData(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'funds'}
        resp = requests.get(
            'http://185.231.115.223:3000/View_FundsMeta?ID=eq.'+str(identifier), headers=head)
        if resp.status_code == 200:

            # print(json.loads(resp.text))
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct = ct+1

    return "noData"

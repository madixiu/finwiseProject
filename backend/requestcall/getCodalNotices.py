
import requests
import json
from .util.unixToUTCunix import engDateToUnix
import uuid
# import time
import pandas as pd


def get_true_value(x):
    return int(x.replace(',', ''))


def CodalNoticesRequest(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/View_CodalNotices?StockID=eq.'+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def SubHeader(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/View_SubHeaderWidget?ID=eq.'+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"

# Monthly


def getTypeOffirm(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/monthlyreporttype?a='+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getAdminsNotices(firm):
    try:
        head = {'Accept-Profile': 'public'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/adminsnotice?a='+str(firm), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def StatusChanges(identifier):
    try:
        head = {'Accept-Profile': 'marketwatch'}
        resp = requests.get('http://185.231.115.223:3000/View_StatusChange?ID=eq.' +
                            str(identifier)+'&limit=7', headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyBankDeposits(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/bankdeposits_monthly?a='+identifier, headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyInsurance(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/insurancemonthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyConstOngoing(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/construction_ongoing_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyConstSold(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/construction_sold_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"


def monthlyService(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/servicemonthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyBankFacility(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/bankfacilities_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyProduction(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/productionmonthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyPAnalysis1(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/productionmonthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF = pd.DataFrame(json.loads(resp.text))
            DF.loc[DF['category'].isnull(), 'category'] = 'Domestic_Sale'
            DF = DF[DF['name'] != 'تخفیفات']
            DX = DF.groupby(by=['name', 'toDate']).sum()
            DX2 = DX[['totalProductionPeriod',
                      'modification_SalesAmount']].reset_index()
            DX4 = pd.DataFrame()
            for t in DX2.name.unique():
                Temp = DX2[DX2['name'] == t]
                Temp = Temp.sort_values(by=['toDate'])
                Temp['Shifted'] = Temp['modification_SalesAmount'].shift(-1)
                Temp.fillna(0, inplace=True)
                DX4 = DX4.append(Temp)
            DX4['Sale'] = DX4['totalProductionPeriod']+DX4['Shifted']
            DX4 = DX4[['name', 'toDate', 'Sale']]
            DX4.sort_values(by=['toDate'], ascending=False, inplace=True)
            DY = DF.groupby(by=['category', 'toDate']).sum()
            DY2 = DY[['totalProductionPeriod',
                      'modification_SalesAmount']].reset_index()
            DY2 = DY2[(DY2['category'] != 'Refund') &
                      (DY2['category'] != 'Discount')]
            DY4 = pd.DataFrame()
            for t in DY2.category.unique():
                Temp = DY2[DY2['category'] == t]
                Temp = Temp.sort_values(by=['toDate'])
                Temp['Shifted'] = Temp['modification_SalesAmount'].shift(-1)
                Temp.fillna(0, inplace=True)
                DY4 = DY4.append(Temp)
            DY4['Sale'] = DY4['totalProductionPeriod']+DY4['Shifted']
            DY4 = DY4[['category', 'toDate', 'Sale']]
            DY4.replace('Export_Sale', 'فروش صادراتی', inplace=True)
            DY4.replace('Domestic_Sale', 'فروش داخلی', inplace=True)
            DY4.replace('Service_revenue', 'درآمد خدمات', inplace=True)
            return {'1': json.loads(DX4.to_json(orient='records')), '2': json.loads(DY4.to_json(orient='records'))}
    except:
        return "noData"


def monthly_leasing_cost(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/leasingcost_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthly_leasing_delegated(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/leasingdelegated_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthly_leasing_revenue(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/leasingrevenue_monthly?a='+(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyInvestInTransactions(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/investment_monthly_in_transactions?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyInvestOutTransactions(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/investment_monthly_out_transactions?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyInvestPortf(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/investment_monthly_portfo_transactions?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def monthlyInvestSummary(identifier):
    try:
        head = {'Accept-Profile': 'monthly'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/investment_monthly_summary_transactions?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"

#################


def getBalanceSheetFirm(identifier):
    try:
        head = {'Accept-Profile': 'statement'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/bsall?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getBalanceSheetAggregatedFirm(identifier):
    try:
        head = {'Accept-Profile': 'statement'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/bsallaggregated?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getIncomeStatementFirm(identifier):
    try:
        head = {'Accept-Profile': 'statement'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/isall?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getIncomeStatementFirmAggrregated(identifier):
    try:
        head = {'Accept-Profile': 'statement'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/isallaggregated?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getCFFirm(identifier):
    try:
        head = {'Accept-Profile': 'statement'}
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/cfall?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getBoard(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/currentboard?a='+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getceo(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/currentceo?a='+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def getAllDps(identifier):
    try:
        resp = requests.get(
            'http://185.8.172.68:3000/rpc/alldps?a='+str(identifier))
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def AdjustedPrices(identifier):
    try:
        head = {'Accept-Profile': 'marketwatch'}
        resp = requests.get(
            'http://185.231.115.223:3000/View_AdjustedPrices?firm=eq.'+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"


def AdjustedPricesBasedOnCodal(identifier, type):
    try:
        head = {'Accept-Profile': 'public'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/adjustedpricestyp3?a='+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            js = json.loads(resp.text)
            for item in js:
                date = item["engdate"].split('-')
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])
                item["unix"] = engDateToUnix(year, month, day, 8, 0)

            if type == 'chart':
                js = sorted(js, key=lambda x: x['unix'], reverse=False)
            elif type == 'table':
                js = sorted(js, key=lambda x: x['unix'], reverse=True)
            return (js)
    except:
        return "noData"

    return "noData"


def HHhistory(identifier):
    try:
        head = {'Accept-Profile': 'public'}
        resp = requests.get(
            'http://185.231.115.223:3000/View_HHhistory?firm=eq.'+str(identifier), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF2 = pd.json_normalize(json.loads(resp.text))
            labels = [DF2.head(11).englishDate.tolist()]
            return([labels, json.loads(resp.text)])
    except:
        return "noData"
    return "noData"


def getNews():
    try:
        head = {'Accept-Profile': 'news'}
        resp = requests.get(
            'http://185.8.172.68:3000/LatestNews', headers=head, timeout=3)
        if resp.status_code == 200 and not resp.text == []:
            js = json.loads(resp.text)
            for item in js:
                item['id'] = uuid.uuid4()
            return (js)
        else:
            return "noData"
    except:
        return "noData"


def getICNew1():
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_Proposal', headers=head)
        if resp.status_code == 200 and not resp.text == []:

            DF2 = pd.read_json(resp.text)
            DF2['Title'] = 'پیشنهاد هیئت مدیره به مجمع'
            DF2.loc[DF2['Correction'],
                    'Title'] = DF2.loc[DF2['Correction'], 'Title']+['-اصلاحیه']
            DF2['FromAmount'] = DF2['FromAmount'].apply(get_true_value)
            DF2['ToAmount'] = DF2['ToAmount'].apply(get_true_value)
            DF2['IncreasePercent'] = (
                DF2['ToAmount']-DF2['FromAmount'])*100/DF2['FromAmount']
            DF2 = DF2[['ticker', 'PublishTime', 'Title',
                       'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']]
            DF2.columns = ['ticker', 'PublishTime', 'Title',
                           'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']
            return DF2
    except:
        return "noData"
    return "noData"


def getICNew2():
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_Assembly', headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF2 = pd.read_json(resp.text)
            DF2['CapitalChangeType'] = ''
            DF2['Title'] = 'تصمیمات مجمع عمومی فوق العاده'
            # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
            DF2.loc[DF2['CashIncoming_Final'] != 0,
                    'CapitalChangeType'] = DF2.loc[DF2['CashIncoming_Final'] != 0, 'CapitalChangeType']+'آورPه -'
            DF2.loc[DF2['RetainedEarning_Final'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['RetainedEarning_Final']
                                                                                      != 0, 'CapitalChangeType']+'سود انباشته -'
            DF2.loc[DF2['Reserves_Final'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['Reserves_Final']
                                                                               != 0, 'CapitalChangeType']+'ذخایر -'
            DF2.loc[DF2['Reevaluation_Final'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['Reevaluation_Final']
                                                                                   != 0, 'CapitalChangeType']+'تجدید ارزیابی -'
            DF2 = DF2[['ticker', 'PublishTime', 'Title',
                       'IncreasePercent_Final', 'CapitalChangeType', 'HtmlUrl']]
            DF2.columns = ['ticker', 'PublishTime', 'Title',
                           'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']
            return DF2
    except:
        return "noData"
    return "noData"


def getICNew3():
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_N70', headers=head)
        if resp.status_code == 200 and not resp.text == []:

            DF2 = pd.read_json(resp.text)
            DF2['FromAmount_Step'] = DF2['FromAmount_Step'].apply(
                get_true_value)
            DF2['ToAmount_Step'] = DF2['ToAmount_Step'].apply(get_true_value)
            DF2['Title'] = 'تصمیم هیئت مدیره به انجام افزایش سرمایه تفویض شده'
            DF2['IncreasePercent'] = (
                DF2['ToAmount_Step']-DF2['FromAmount_Step'])*100/DF2['FromAmount_Step']
            DF2.loc[DF2['Correction'],
                    'Title'] = DF2.loc[DF2['Correction'], 'Title']+['-اصلاحیه']
            DF2 = DF2[['ticker', 'PublishTime', 'Title',
                       'IncreasePercent', 'CapitalChangeType_Step', 'HtmlUrl']]
            DF2.columns = ['ticker', 'PublishTime', 'Title',
                           'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']
            return DF2
    except:
        return "noData"
    return "noData"


def getICNew4():
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_N73', headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF2 = pd.read_json(resp.text)
            DF2['CapitalChangeType'] = ''
            DF2['Title'] = 'تصمیمات هیئت مدیره درخصوص افزایش سرمایه'
            DF2.loc[DF2['Correction'],
                    'Title'] = DF2.loc[DF2['Correction'], 'Title']+['-اصلاحیه']
            DF2.loc[DF2['cashIncoming'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['cashIncoming']
                                                                             != 0, 'CapitalChangeType']+'آورده -'
            DF2.loc[DF2['RetainedEarning'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['RetainedEarning']
                                                                                != 0, 'CapitalChangeType']+'سود انباشته -'
            DF2.loc[DF2['Reserves'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['Reserves']
                                                                         != 0, 'CapitalChangeType']+'ذخایر -'
            DF2.loc[DF2['RevaluationSurplus'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['RevaluationSurplus']
                                                                                   != 0, 'CapitalChangeType']+'تجدید ارزیابی -'
            DF2 = DF2[['ticker', 'PublishTime', 'Title',
                       'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']]
            DF2.columns = ['ticker', 'PublishTime', 'Title',
                           'IncreasePercent', 'CapitalChangeType', 'HtmlUrl']
            return DF2
    except:
        return "noData"
    return "noData"


def get_IC_ALL():
    DFT = None
    DF1 = getICNew1()
    DF2 = getICNew2()
    DF3 = getICNew3()
    DF4 = getICNew4()
    if DF2 != "noData":
        DFT = DF1.append(DF2)
    if DF3 != "noData":
        DFT = DFT.append(DF3)
    if DF4 != "noData":
        DFT = DFT.append(DF4)
    if DFT != None:
        DFT.sort_values(by=['PublishTime'], ascending=False)
        return json.loads(DFT.to_json(orient="records"))
    else:
        return "noData"


def get_IC_Assembly_Stock(firm):
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_N73?StockID=eq.'+str(firm), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF2 = pd.read_json(resp.text)
            if not DF2.empty:
                DF2['CapitalChangeType'] = ''
                DF2['Title'] = 'تصمیمات هیئت مدیره درخصوص افزایش سرمایه'
                # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
                DF2.loc[DF2['cashIncoming'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['cashIncoming']
                                                                                 != 0, 'CapitalChangeType']+'آورده -'
                DF2.loc[DF2['RetainedEarning'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['RetainedEarning']
                                                                                    != 0, 'CapitalChangeType']+'سود انباشته -'
                DF2.loc[DF2['Reserves'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['Reserves']
                                                                             != 0, 'CapitalChangeType']+'ذخایر -'
                DF2.loc[DF2['RevaluationSurplus'] != 0, 'CapitalChangeType'] = DF2.loc[DF2['RevaluationSurplus']
                                                                                       != 0, 'CapitalChangeType']+'تجدید ارزیابی -'
                DF2 = DF2[['ticker', 'PublishTime', 'Title', 'IncreasePercent',
                           'CapitalChangeType', 'HtmlUrl', "StockID"]]
                DF2.columns = ['ticker', 'PublishTime', 'Title',
                               'IncreasePercent', 'CapitalChangeType', 'HtmlUrl', "StockID"]
            return DF2
    except:
        return "noData"
    return "noData"


def get_IC_N73_Stock(firm):
    try:
        head = {'Accept-Profile': 'codalreports'}
        resp = requests.get(
            'http://185.8.172.68:3000/View_IC_Assembly?StockID=eq.'+str(firm), headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF4 = pd.read_json(resp.text)
            if not DF4.empty:
                DF4['CapitalChangeType'] = ''
                DF4['Title'] = 'تصمیمات مجمع عمومی فوق العاده'
                # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
                DF4.loc[DF4['CashIncoming_Final'] != 0,
                        'CapitalChangeType'] = DF4.loc[DF4['CashIncoming_Final'] != 0, 'CapitalChangeType']+'آورده -'
                DF4.loc[DF4['RetainedEarning_Final'] != 0, 'CapitalChangeType'] = DF4.loc[DF4['RetainedEarning_Final']
                                                                                          != 0, 'CapitalChangeType']+'سود انباشته -'
                DF4.loc[DF4['Reserves_Final'] != 0, 'CapitalChangeType'] = DF4.loc[DF4['Reserves_Final']
                                                                                   != 0, 'CapitalChangeType']+'ذخایر -'
                DF4.loc[DF4['Reevaluation_Final'] != 0, 'CapitalChangeType'] = DF4.loc[DF4['Reevaluation_Final']
                                                                                       != 0, 'CapitalChangeType']+'تجدید ارزیابی -'
                DF4 = DF4[['ticker', 'PublishTime', 'Title', 'IncreasePercent_Final',
                           'CapitalChangeType', 'HtmlUrl', "StockID"]]
                DF4.columns = ['ticker', 'PublishTime', 'Title',
                               'IncreasePercent', 'CapitalChangeType', 'HtmlUrl', "StockID"]
            return DF4
    except:
        return "noData"
    return "noData"


def get_IC_Done(firm):
    DF4 = get_IC_N73_Stock(firm)
    DF2 = get_IC_Assembly_Stock(firm)
    DFT = DF4.append(DF2)
    if not DFT.empty:
        DFT.sort_values(by=['PublishTime'], ascending=False)
        DFT = DFT[DFT['IncreasePercent'] != 0]
    return json.loads(DFT.to_json(orient="records"))

import requests
import time
import pandas
import json
import pandas as pd
from khayyam import JalaliDate
import re
from datetime import date, datetime


listofDicts = []

# ----------------------------------------------------- first function with one input -------------------------------------------------------- noqa

def publicApi(i):
    flag = True
    while flag:
        # start = time.time()
        resp = requests.get('http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i='+str(i)+'&c=27+')
        if resp.status_code != 200:
            flag = True
            continue
        else:
            flag = False
            whole = resp.text
            # print(whole)
        counter = 0
        dictt = {}
        for i in (whole.split(';')[0]).split(','):
            dictt[counter] = i
            listofDicts.append(dictt)
            counter = counter+1
        df = pandas.DataFrame([dictt])
        df.columns = ['lastUpdate','L','Moamele','Closing','First','yesterday','Max','Min','Count','Volume','Value','L2','Date','lastUpdatedAt']    # noqa
        return df.to_dict('records')[0]


# ---------------------------------------------------- realtime api function with no input-------------------------------------------------


def isfloat(x):
    try:
        a = float(x) # noqa
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def get_true_value(x):
    Million = False
    Billion = False
    x = str(x)
    if ('ا' in x) or ('و' in x) or ('ی' in x):
        return x
    negative = False
    if(',' in x):
        x = x.replace(',', '')
    if('(' in x and ')' in x):
        x = x.replace(')', '')
        x = x.replace('(', '')
        negative = True
    if (' B') in x:
        x = x.replace(' B', '')
        Billion = True
    if (' M') in x:
        x = x.replace(' M', '')
        Million = True
    if isint(x):
        x = x.split('.')[0]
        if negative:
            x = int(x)*-1
        else:
            x = int(x)
        if Million:
            x = int(x)*1000000
        if Billion:
            x = int(x)*1000000000
    elif type(x) == float:
        if negative:
            x = float(x)*-1
        else:
            x = float(x)
        if Million:
            x = float(x)*1000000
        if Billion:
            x = float(x)*1000000000
    return x


def Translate_response(wholeHtml, wholeHtml2):
    wholeHtml = wholeHtml.replace('\r', '')
    wholeHtml = wholeHtml.replace('\n', '')
    listofDictsAll = []
    for i in re.findall("<tr>(.+?)</tr>", wholeHtml):
        Dicts = {}
        if '<th>' not in i:
            item = i
            counter = 0
            for j in re.findall('<td>(.+?)</td>', item):
                if '<a' in j:
                    value = re.findall('>(.+?)</a>', j)[0]
                    Dicts[counter] = get_true_value(value)
                    counter = counter+1
                else:
                    if '<div' in j:
                        value = re.findall('>(.+?)</div>', j)[0]
                        Dicts[counter] = get_true_value(value)
                        counter = counter+1
                    else:
                        value = j
                        Dicts[counter] = get_true_value(value)
                        counter = counter+1

        listofDictsAll.append(Dicts)
    DF = pd.DataFrame(listofDictsAll)
    DF.dropna(inplace=True)
    DF.replace('ك' ,'ک', regex = True, inplace=True) # noqa
    DF.replace('ي','ی', regex = True, inplace=True) # noqa
    DF.columns = ['ID', 'Hour', 'Value', 'change', 'changePerc', 'Max', 'Min']
    DF['engDate'] = str(datetime.now()).split(' ')[0]
    for index, row in DF.iterrows():
        englishDate = row['engDate']
        year = englishDate[0:4]
        month = englishDate[5:7]
        day = englishDate[8:10]
        # print(day)
        persianDate = (JalaliDate(date(int(year), int(month), int(day))))
        DF.loc[index, 'persianDate'] = str(persianDate).replace('-', '')
    wholeHtml2 = wholeHtml2.replace('\r', '')
    wholeHtml2 = wholeHtml2.replace('\n', '')
    listofDictsAll = []
    for i in re.findall("<tr>(.+?)</tr>", wholeHtml2):
        Dicts = {}
        if '<th>' not in i:
            item = i
            counter = 0
            for j in re.findall('<td>(.+?)</td>', item):
                if '<a' in j:
                    value = re.findall('>(.+?)</a>', j)[0]
                    Dicts[counter] = get_true_value(value)
                    counter = counter+1
                else:
                    if '<div' in j:
                        value = re.findall('>(.+?)</div>', j)[0]
                        Dicts[counter] = get_true_value(value)
                        counter = counter+1
                    else:
                        value = j
                        Dicts[counter] = get_true_value(value)
                        counter = counter+1

        listofDictsAll.append(Dicts)
    DF2 = pd.DataFrame(listofDictsAll)
    DF2.dropna(inplace=True)
    DF2.replace('ك','ک', regex = True,inplace=True) # noqa
    DF2.replace('ي','ی', regex = True,inplace=True) # noqa
    DF2.columns = ['ID', 'MarketValue', 'Count', 'Volume', 'TradeValue']
    DF3 = pd.merge(DF, DF2, on='ID', how='outer')
    DF3.replace('شاخص قیمت هم وزن','شاخص قیمت (هم وزن)', regex = True, inplace = True) # noqa
    return DF3


def realTimePublicApi():
    flag = True
    while flag:
        resp = requests.get('http://www.tsetmc.com/Loader.aspx?Partree=151315&Flow=1') # noqa
        resp2 = requests.get('http://www.tsetmc.com/Loader.aspx?Partree=15131O') # noqa
        if resp.status_code != 200 | resp2.status_code != 200:
            time.sleep(2)
            print('error')
        else:
            flag = False
            wholeHtml = resp.text
            wholeHtml2 = resp2.text
        DF6 = Translate_response(wholeHtml, wholeHtml2) # noqa
        if not DF6.empty:
            return json.dumps(DF6.to_dict('records'),ensure_ascii = False).encode('utf-8').decode()
            # return DF6.to_dict('records')
        else:
            flag = True

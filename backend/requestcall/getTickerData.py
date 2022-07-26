import requests
import json
import time
from .util.FixGetTechnicalIndicatorsAll import fixData 

def getTechnicalIndicators(identifier):
    try:
        head = {'Accept-Profile':'technical'}
        resp = requests.get('http://185.231.115.223:3000/View_Technical_Indicators?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
        return []      
    return []

def getTechnicalIndicators2(identifier):
   
    head = {'Accept-Profile':'technical'}
    resp = requests.get('http://185.231.115.223:3000/View_Technical_Indicators?firm=eq.'+str(identifier),headers=head)
    if resp.status_code == 200 and resp.text!='[]' :
        #?%%%%%%%%%%%%%%%%%%%%%%%%%%% NEW DATA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Indicators = ["Signal_PSAR","Signal_PSAR","Signal_Aroon","Signal_Williams","Signal_Ultimate","Signal_Awesome","Signal_CCI","Signal_MOM","Signal_MFI","Signal_ADX","Signal_StochRSI","Signal_MACD","Signal_Stoch","Signal_RSI"]
        mas= [
        "Signal_HMA",
        "Signal_VAMA",
        "Signal_KETLER",
        "Signal_ICHI",
        "Signal_SMA200",
        "Signal_SMA100",
        "Signal_SMA50",
        "Signal_SMA20",
        "Signal_SMA10",
        "Signal_SMA5",
        "Signal_EMA200",
        "Signal_EMA100",
        "Signal_EMA50",
        "Signal_EMA20",
        "Signal_EMA10",
        "Signal_EMA5"
        ]
        score = {
        'sum': 0,
        'neutral': 0,
        'positive': 0,
        'negative': 0,
        'sumMa': 0,
        'neutralMa': 0,
        'positiveMa': 0,
        'negativeMa': 0,
        'sumIndic': 0,
        'neutralIndic': 0,
        'positiveIndic': 0,
        'negativeIndic': 0,
        }
        info =['firm','engdate','persiandate','sum_signal']
        js = json.loads(resp.text)
        item = js[0]
        result = []
        MAS = {}
        INDICATORS = {}
        mainItems = []
        Info = {}

        for (key, value) in item.items():
            if key in mas:
                MAS[key] = value

                if value == 1:
                    score['positive'] +=1
                    score['sum'] +=1
                    score['positiveMa']+=1
                    score['sumMa']+=1
                elif value == -1:
                    score['negative'] +=1
                    score['sum'] -=1
                    score['negativeMa'] +=1
                    score['sumMa'] -=1
                elif value ==0:
                    score['neutral'] +=1
                    score['neutralMa'] +=1
            elif key in Indicators:
                INDICATORS[key] = value
                if value == 1:
                    score['positive'] +=1
                    score['sum'] +=1
                    score['positiveIndic'] +=1
                    score['sumIndic']+=1
                elif value == -1:
                    score['negative']+=1
                    score['sum']-=1
                    score['negativeIndic']+=1
                    score['sumIndic']-=1
                elif value == 0:
                    score['neutral']+=1
                    score['neutralIndic'] +=1

            elif key in info:
                Info[key] = value
            else:
                mainItems.append({"title": key,"Value": round(value,2)})

            result = {'info':Info,'tableData':mainItems,'mas':MAS,'indicators':INDICATORS,'score':score}

            # result.append(item)
        #?%%%%%%%%%%%%%%%%%%%%%%%%%%% NEW DATA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        return result     
    return "noData"   

def getTechnicalIndicatorsAll():
    try:
        head = {'Accept-Profile':'technical'}
        resp = requests.get('http://185.231.115.223:3000/View_Technical_IndicatorsAll',headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return fixData(json.loads(resp.text))
    except:
        return "noData"  
    return "noData"  

def getIndicesHistoric():
    try:
        head = {'Accept-Profile':'indices'}
        resp=requests.get('http://185.231.115.223:3000/View_HistoricIndicesReturn',headers=head)
        if resp.status_code == 200:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"

def tickerNameRequest(): 
    try:
        resp = requests.get('http://185.8.172.68:3000/View_tickerOnly')
        if resp.status_code == 200:
            return (json.loads(resp.text))
    except:
        return "noData"
    return "noData"

def getCalculatedValuationRatios(identifier):
    try:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://185.8.172.68:3000/View_ValuationRatios?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
        return []
    return []
    
def getFundamentalRatiosToDisplay(identifier):
    try:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://185.8.172.68:3000/RatiosToDisplay?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
        return []
    return []

def getFundamentalLatestComponents(identifier):
    try:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://185.8.172.68:3000/View_LatestValuationComponent?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
   
        return []    
    return []

def getStockHH(identifier):
    try:
        head = {'Accept-Profile':'marketwatch'}
        resp = requests.get('http://185.231.115.223:3000/View_HH_Historic?ID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
        return []
    return []        
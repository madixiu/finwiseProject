
import requests
import json
from .util.Convereter_trunc import truncater
from .util.unixToUTCunix import timeToUnix
# import time
def Top5MostViewed():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/ViewTop5MostViewed',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")
def ImpactOnIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/ViewImpactOnIndex',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData") 
def getLiveHHtickerData(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_Live_Stock_HH?ID=eq.'+str(identifier),headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")       
def getShareholdersList(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_ShareHolders?ID=eq.'+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")       

def getStatisticsTicker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://185.231.115.223:3000/rpc/statisticsticker?a='+str(identifier),headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")           
def getLive_ticker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://185.231.115.223:3000/rpc/liveticker?a='+str(identifier),headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")           
def highestTvolumes():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/ViewHighestTradeVolumes',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData") 
def getMarketHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/ViewDashboard_HHDetailsStock',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")  
def highestTvalues():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/ViewHighestTradeValues',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")      
def highestDemands():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_HighestDemands',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")        
def highestSupplies():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_HighestSupplies',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")                                
def get_AdminsNotice(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://185.231.115.223:3000/rpc/adminsnotice?a='+str(identifier),headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")   

def AllIndicesImpact():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_IndicesImpactOnIndex',headers=head )
    if resp.status_code == 200:
        js = json.loads(resp.text)
        js = sorted(js, key=lambda x: x['IMPACT'], reverse = True)
        return (js)
    else:
        return("noData")    
def AllIndicesHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_Industries_HH',headers=head )
    if resp.status_code == 200:
        js = json.loads(resp.text)
        js = sorted(js, key=lambda x: x['sum'], reverse = True)
        return (js)
    else:
        return("noData")    


# ****************************************************************************************************************
# *********************************************INDUSTRY DETAIL*****************************************************                 
def getIndicesDetails(identifier):
    head = {'Accept-Profile':'indices'}
    head2 = {'Accept-Profile':'technical'}
    # ************** REQUESTS *****************
    resp = requests.get('http://185.231.115.223:3000/View_Index_Include?ID=eq.'+str(identifier),headers=head)
    technicalResp = requests.get('http://185.231.115.223:3000/View_indices_allstocks_indicators?ID=eq.'+str(identifier),headers = head2)
    ShakhesResp = requests.get('http://185.231.115.223:3000/View_indexValue_Today?ID=eq.'+str(identifier),headers = head)
    # ************** REQUESTS *****************


    if resp.status_code == 200:
        js = json.loads(resp.text)
        js = alterData(js)

    if technicalResp.status_code == 200:
        technicalJS = json.loads(technicalResp.text)
        js = AddTechnicalData(js,technicalJS)
        result = DataModifier(js)

    if ShakhesResp.status_code == 200:
        ShakhesJS = json.loads(ShakhesResp.text)
        ShakhesJS = ShakhesDataModifier(ShakhesJS)
        # result.append({"Tepix":ShakhesJS})
        result["Tepix"] = ShakhesJS

        return result
        # return(json.loads(resp.text))
    else:
        return("NoData")  

def alterData(input):
    input = sorted(input, key=lambda x : x['ticker'], reverse=False)
    # for index,item in enumerate(input):
    for item in input:
        if item["close"] == None:
            item["close"] = 0
        if item["yesterday"] == None:
            item["yesterday"] = 0

        if item["close"] and item["yesterday"] !=0:
            item["lastPercent"] = truncater(((item["close"] - item["yesterday"])/item["close"]) * 100)
        else:
            item["lastPercent"] = 0
        
        if item["VolumeBuy_Haghighi"] == None:
            item["VolumeBuy_Haghighi"] = 0
        if item["VolumeSell_Haghighi"] == None:
            item["VolumeSell_Haghighi"] = 0

        item["HH"] = (item["VolumeBuy_Haghighi"] - item["VolumeSell_Haghighi"]) * item["close"]
    
    return input
    
def AddTechnicalData(input,extraInput):
    # input = sorted(input, key=lambda x : x['ticker'], reverse=False)
    extraInput = sorted(extraInput, key=lambda x : x['ticker'], reverse=False)
    for index in range(len(input)):
        if extraInput:
            if index >= len(extraInput):
                input[index]["signal"] = 0
            else:
                input[index]["signal"] = extraInput[index]["signal"]
    return input

def DataModifier(input):
    
    result = {}
    Impact = []
    marketCap = []
    HH = []
    technical = []
    table = []
    ImpactSum = 0
    HHSum = 0
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for item in input:
        if item["last"] == None:
            item["last"] = 0
        if item["marketcap"] == None:
            item["marketcap"] = 0
        if item["Impact"] == None:
            item["Impact"] = 0
        if item["signal"] == "NaN":
            item["signal"] = 0

        Impact.append({"id":item["firm"],"ticker":item["ticker"],"Impact":item["Impact"]})
        marketCap.append({"id":item["firm"],"ticker":item["ticker"],"marketcap":item["marketcap"]})
        HH.append({"id":item["firm"],"ticker":item["ticker"],"HH":item["HH"]})
        technical.append({"id":item["firm"],"ticker":item["ticker"],"signal":item["signal"]})
        table.append({"id":item["firm"],"ticker":item["ticker"],"last":item["last"],"lastPercent":item["lastPercent"],"marketcap":item["marketcap"]})
        ImpactSum += item["Impact"]
        HHSum += item["HH"]

    Impact = sorted(Impact, key=lambda x : x['Impact'], reverse=True)
    marketCap = sorted(marketCap, key=lambda x : x['marketcap'], reverse=True)
    HH = sorted(HH, key=lambda x : x['HH'], reverse=True)
    technical = sorted(technical, key=lambda x : x['signal'], reverse=True)
    table = sorted(table, key=lambda x : x['marketcap'], reverse=True)


    result["Impact"] = {"ImpactData" : Impact, "Sum":ImpactSum}
    result["marketCap"] = {"marketCapData" : marketCap}
    result["HH"] = {"HHData":HH, "Sum":HHSum}
    result["Technical"] = {"TechnicalData":technical}
    result["Table"] = {"TableData":table}
    return result


def ShakhesDataModifier(input):
    export = []
    RaWdata = []
    apexData = []
    
    input = input [0:15]
    for item in input:
        time = item['HourMinute']
        hour = int(time[0:2])
        minute = int(time[3:5])
        UTCtimeUNIX = timeToUnix(hour,minute)
        RaWdata.append({"HourMinute":item["HourMinute"],"Value":item["Value"],"unix":UTCtimeUNIX})
        apexData.append([UTCtimeUNIX,item["Value"]])
    export = {'CorrectName':item['CorrectName'],'RaWdata': RaWdata,"apexData":apexData}
    return export

# ****************************************************************************************************************
# ****************************************************************************************************************
def TradeValueHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_TradeValuesHH_Total',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")  
def TradeValueHHBasedOnAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_TradeValuesHH_Assets',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")  
def TradeValueAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_TradeValues_Assets',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")  
def getLatestTwoIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_LiveIndex',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")                                  

def getLastActiveDayTepix():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://185.231.115.223:3000/View_today_Tepix',headers=head )
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("noData")          
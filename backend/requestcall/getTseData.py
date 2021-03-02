
import requests
import json
from .util.Convereter_trunc import truncater
# import time
def Top5MostViewed():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewTop5MostViewed',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")
def ImpactOnIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewImpactOnIndex',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data") 
def getLiveHHtickerData(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_Live_Stock_HH?ID=eq.'+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")       
def getShareholdersList(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_ShareHolders?ID=eq.'+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")       

def getStatisticsTicker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/statisticsticker?a='+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")           
def getLive_ticker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/liveticker?a='+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")           
def highestTvolumes():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeVolumes',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestTvalues():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeValues',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestDemands():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestDemands',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestSupplies():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestSupplies',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                                
def get_AdminsNotice(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/adminsnotice?a='+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")   

# ****************************************************************************************************************                 
def getIndicesDetails(identifier):
    head = {'Accept-Profile':'indices'}
    head2 = {'Accept-Profile':'technical'}
    # ************** REQUESTS *****************
    resp = requests.get('http://37.152.180.99:3000/View_Index_Include?ID=eq.'+str(identifier),headers=head)
    technicalResp = requests.get('http://37.152.180.99:3000/View_indices_allstocks_indicators?ID=eq.'+str(identifier),headers = head2)
    ShakhesResp = requests.get('http://37.152.180.99:3000/View_indexValue_Today?ID=eq.'+str(identifier),headers = head)
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
        return ([result,ShakhesJS])
        # return(json.loads(resp.text))
    else:
        return("NoData")  

def alterData(input):
    input = sorted(input, key=lambda x : x['ticker'], reverse=False)
    # for index,item in enumerate(input):
    for item in input:
        if item["close"] and item["yesterday"] !=None:
            item["lastPercent"] = truncater(((item["close"] - item["yesterday"])/item["close"]) * 100)
            item["HH"] = (item["VolumeBuy_Haghighi"] - item["VolumeSell_Haghighi"]) * item["close"]
    return input
    
def AddTechnicalData(input,extraInput):
    # input = sorted(input, key=lambda x : x['ticker'], reverse=False)
    extraInput = sorted(extraInput, key=lambda x : x['ticker'], reverse=False)
    for index in range(len(input)):
        if extraInput:
            input[index]["signal"] = extraInput[index]["signal"]
    return input

def DataModifier(input):
    result = {}
    temp = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    ImpactSum = 0
    HHSum = 0
    for item in input:
        temp.append({"ticker":item["ticker"],"Impact":item["Impact"]})
        temp2.append({"ticker":item["ticker"],"marketcap":item["marketcap"]})
        temp3.append({"ticker":item["ticker"],"HH":item["HH"]})
        temp4.append({"ticker":item["ticker"],"signal":item["signal"]})
        temp5.append({"ticker":item["ticker"],"last":item["last"],"lastPercent":item["lastPercent"]})
        ImpactSum += item["Impact"]
        HHSum += item["HH"]

    temp = sorted(temp, key=lambda x : x['Impact'], reverse=True)
    temp2 = sorted(temp2, key=lambda x : x['marketcap'], reverse=True)
    temp3 = sorted(temp3, key=lambda x : x['HH'], reverse=True)
    temp4 = sorted(temp4, key=lambda x : x['signal'], reverse=True)


    result["Impact"] = {"ImpactData" : temp, "Sum":ImpactSum}
    result["marketCap"] = {"marketCapData" : temp2}
    result["HH"] = {"HHData":temp3, "Sum":HHSum}
    result["Technical"] = {"TechnicalData":temp4}
    result["Table"] = {"TableData":temp5}
    return result




# ****************************************************************************************************************
def TradeValueHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValuesHH_Total',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def TradeValueHHBasedOnAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValuesHH_Assets',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def TradeValueAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValues_Assets',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def getLatestTwoIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_LiveIndex',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                                  

def getLastActiveDayTepix():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_today_Tepix',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")          
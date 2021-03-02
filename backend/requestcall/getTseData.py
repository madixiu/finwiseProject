
import requests
import json
# from .util.Convereter_trunc import truncater, converter
# import time
def Top5MostViewed():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewTop5MostViewed',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")
def ImpactOnIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewImpactOnIndex',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data") 
def getLiveHHtickerData(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_Live_Stock_HH?ID=eq.'+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")       
def getShareholdersList(identifier):
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_ShareHolders?ID=eq.'+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")       

def getStatisticsTicker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/statisticsticker?a='+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")           
def getLive_ticker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/liveticker?a='+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")           
def highestTvolumes():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeVolumes',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data") 
def getMarketHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewDashboard_HHDetailsStock',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def highestTvalues():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeValues',headers=head,timeout=8)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        print('an')
        return("No Data")        
def highestDemands():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestDemands',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestSupplies():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestSupplies',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                                
def get_AdminsNotice(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/adminsnotice?a='+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                    
def getIndicesDetails(identifier):
    head = {'Accept-Profile':'indices'}
    resp = requests.get('http://37.152.180.99:3000/View_Index_Include?ID=eq.'+str(identifier),headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  

def TradeValueHH():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValuesHH_Total',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def TradeValueHHBasedOnAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValuesHH_Assets',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def TradeValueAsset():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_TradeValues_Assets',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")  
def getLatestTwoIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_LiveIndex',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                                  

def getLastActiveDayTepix():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_today_Tepix',headers=head ,timeout=5)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")          
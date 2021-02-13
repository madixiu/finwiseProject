
import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
import pandas as pd
def CodalNoticesRequest(identifier):
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/View_CodalNotices?StockID=eq.'+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
            # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")

def SubHeader(identifier):
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/View_SubHeaderWidget?ID=eq.'+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
##### Monthly
def getTypeOffirm(identifier):
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/rpc/monthlyreporttype?a='+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def getAdminsNotices(firm):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'public'}
        resp = requests.get('http://37.152.180.99:3000/rpc/adminsnotice?a='+str(firm),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")    
def StatusChanges(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'marketwatch'}
        resp = requests.get('http://37.152.180.99:3000/View_StatusChange?ID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")      
def monthlyBankDeposits(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Bank_Deposit?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def monthlyInsurance(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Insurance?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData") 
def monthlyConstOngoing(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Const_Ongoing?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData") 
def monthlyConstSold(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Const_Sold?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")    
def monthlyBankFacility(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Bank_Facility?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData") 
def monthlyProduction(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/View_Monthly_Production?StockID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")


def monthlyInvestInTransactions(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/rpc/investment_monthly_in_transactions?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def monthlyInvestOutTransactions(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/rpc/investment_monthly_out_transactions?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def monthlyInvestPortf(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/rpc/investment_monthly_portfo_transactions?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")  
def monthlyInvestSummary(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://185.97.117.60:3000/rpc/investment_monthly_summary_transactions?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")      
      
#################    
def getBoard(identifier): 
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/rpc/currentboard?a='+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def getceo(identifier): 
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/rpc/currentceo?a='+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")    
def getAllDps(identifier): 
    ct=0
    while ct<3:
        resp = requests.get('http://185.97.117.60:3000/rpc/alldps?a='+str(identifier))
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")        
def AdjustedPrices(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'public'}
        resp = requests.get('http://37.152.180.99:3000/View_AdjustedPrices?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")    
def HHhistory(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'public'}
        resp = requests.get('http://37.152.180.99:3000/View_HHhistory?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
            DF=pd.json_normalize(json.loads(resp.text))
            labels=[DF.head(11).englishDate.tolist()]
            # return(resp.text)
            # return (json.loads(resp.text))
            return([labels,json.loads(resp.text)])
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
# if __name__=="__main__":
#     #print()
    
# print(optionRequest())
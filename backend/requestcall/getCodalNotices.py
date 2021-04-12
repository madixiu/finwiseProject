
import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
import pandas as pd
def get_true_value(x):
    return int(x.replace(',',''))
def CodalNoticesRequest(identifier):
    ct=0
    while ct<3:
        resp = requests.get('http://130.185.74.40:3000/View_CodalNotices?StockID=eq.'+str(identifier))
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
        resp = requests.get('http://130.185.74.40:3000/View_SubHeaderWidget?ID=eq.'+str(identifier))
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
        resp = requests.get('http://130.185.74.40:3000/rpc/monthlyreporttype?a='+str(identifier))
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
        resp = requests.get('http://185.231.115.223:3000/rpc/adminsnotice?a='+str(firm),headers=head)
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
        resp = requests.get('http://185.231.115.223:3000/View_StatusChange?ID=eq.'+str(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/bankdeposits_monthly?a='+identifier,headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/insurancemonthly?a='+(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/construction_ongoing_monthly?a='+(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/construction_sold_monthly?a='+(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
def monthlyService(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://130.185.74.40:3000/rpc/servicemonthly?a='+(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/bankfacilities_monthly?a='+(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/productionmonthly?a='+(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")



def monthly_leasing_cost(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://130.185.74.40:3000/rpc/leasingcost_monthly?a='+(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def monthly_leasing_delegated(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://130.185.74.40:3000/rpc/leasingdelegated_monthly?a='+(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def monthly_leasing_revenue(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'monthly'}
        resp = requests.get('http://130.185.74.40:3000/rpc/leasingrevenue_monthly?a='+(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/investment_monthly_in_transactions?a='+str(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/investment_monthly_out_transactions?a='+str(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/investment_monthly_portfo_transactions?a='+str(identifier),headers=head)
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
        resp = requests.get('http://130.185.74.40:3000/rpc/investment_monthly_summary_transactions?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")      
      
#################    
def getBalanceSheetFirm(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/rpc/bsall?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData") 
def getIncomeStatementFirm(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/rpc/isall?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")     
def getCFFirm(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/rpc/cfall?a='+str(identifier),headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")     

    
def getBoard(identifier): 
    ct=0
    while ct<3:
        resp = requests.get('http://130.185.74.40:3000/rpc/currentboard?a='+str(identifier))
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
        resp = requests.get('http://130.185.74.40:3000/rpc/currentceo?a='+str(identifier))
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
        resp = requests.get('http://130.185.74.40:3000/rpc/alldps?a='+str(identifier))
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
        head = {'Accept-Profile':'marketwatch'}
        resp = requests.get('http://185.231.115.223:3000/View_AdjustedPrices?firm=eq.'+str(identifier),headers=head)
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
        resp = requests.get('http://185.231.115.223:3000/View_HHhistory?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200:
            DF2=pd.json_normalize(json.loads(resp.text))
            labels=[DF2.head(11).englishDate.tolist()]
            # return(resp.text)
            # return (json.loads(resp.text))
            return([labels,json.loads(resp.text)])
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def getNews():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'news'}
        resp = requests.get('http://130.185.74.40:3000/LatestNews',headers=head)
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")    


def getICNew1():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_Proposal',headers=head)
        if resp.status_code == 200:
    
            DF2=pd.read_json(resp.text)
            DF2['Title']='پیشنهاد هیئت مدیره به مجمع'
            DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
            DF2['FromAmount']=DF2['FromAmount'].apply(get_true_value)
            DF2['ToAmount']=DF2['ToAmount'].apply(get_true_value)
            DF2['IncreasePercent']=(DF2['ToAmount']-DF2['FromAmount'])*100/DF2['FromAmount']
            DF2=DF2[['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']]
            DF2.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']
            return DF2
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")   
def getICNew2():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_Assembly',headers=head)
        if resp.status_code == 200:
            DF2=pd.read_json(resp.text)
            DF2['CapitalChangeType']=''
            DF2['Title']='تصمیمات مجمع عمومی فوق العاده'
            # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
            DF2.loc[DF2['CashIncoming_Final']!=0,'CapitalChangeType']=DF2.loc[DF2['CashIncoming_Final']!=0,'CapitalChangeType']+'آورPه -'
            DF2.loc[DF2['RetainedEarning_Final']!=0,'CapitalChangeType']=DF2.loc[DF2['RetainedEarning_Final']!=0,'CapitalChangeType']+'سود انباشته -'
            DF2.loc[DF2['Reserves_Final']!=0,'CapitalChangeType']=DF2.loc[DF2['Reserves_Final']!=0,'CapitalChangeType']+'ذخایر -'
            DF2.loc[DF2['Reevaluation_Final']!=0,'CapitalChangeType']=DF2.loc[DF2['Reevaluation_Final']!=0,'CapitalChangeType']+'تجدید ارزیابی -'
            DF2=DF2[['ticker','PublishTime','Title','IncreasePercent_Final','CapitalChangeType','HtmlUrl']]
            DF2.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']
            return DF2
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")
def getICNew3():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_N70',headers=head)
        if resp.status_code == 200:
    
            DF2=pd.read_json(resp.text)
            DF2['FromAmount_Step']=DF2['FromAmount_Step'].apply(get_true_value)
            DF2['ToAmount_Step']=DF2['ToAmount_Step'].apply(get_true_value)
            DF2['Title']='تصمیم هیئت مدیره به انجام افزایش سرمایه تفویض شده'
            DF2['IncreasePercent']=(DF2['ToAmount_Step']-DF2['FromAmount_Step'])*100/DF2['FromAmount_Step']
            DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
            DF2=DF2[['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType_Step','HtmlUrl']]
            DF2.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']
            return DF2
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")   
def getICNew4():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_N73',headers=head)
        if resp.status_code == 200:
            DF2=pd.read_json(resp.text)
            DF2['CapitalChangeType']=''
            DF2['Title']='تصمیمات هیئت مدیره درخصوص افزایش سرمایه'
            DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
            DF2.loc[DF2['cashIncoming']!=0,'CapitalChangeType']=DF2.loc[DF2['cashIncoming']!=0,'CapitalChangeType']+'آورده -'
            DF2.loc[DF2['RetainedEarning']!=0,'CapitalChangeType']=DF2.loc[DF2['RetainedEarning']!=0,'CapitalChangeType']+'سود انباشته -'
            DF2.loc[DF2['Reserves']!=0,'CapitalChangeType']=DF2.loc[DF2['Reserves']!=0,'CapitalChangeType']+'ذخایر -'
            DF2.loc[DF2['RevaluationSurplus']!=0,'CapitalChangeType']=DF2.loc[DF2['RevaluationSurplus']!=0,'CapitalChangeType']+'تجدید ارزیابی -'
            DF2=DF2[['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']]
            DF2.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl']
            return DF2
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")   


def get_IC_ALL():
    DF1=getICNew1()
    DF2=getICNew2()
    DF3=getICNew3()
    DF4=getICNew4()
    DFT=DF1.append(DF2)
    DFT=DFT.append(DF3)
    DFT=DFT.append(DF4)
    DFT.sort_values(by=['PublishTime'],ascending=False)
    return json.loads(DFT.to_json(orient="records"))
    

def get_IC_Assembly_Stock(firm):
     ct=0
     while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_N73?StockID=eq.1'+str(firm),headers=head)
        if resp.status_code == 200:
            DF2=pd.read_json(resp.text)
            if not DF2.empty:
                DF2['CapitalChangeType']=''
                DF2['Title']='تصمیمات هیئت مدیره درخصوص افزایش سرمایه'
                # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
                DF2.loc[DF2['cashIncoming']!=0,'CapitalChangeType']=DF2.loc[DF2['cashIncoming']!=0,'CapitalChangeType']+'آورده -'
                DF2.loc[DF2['RetainedEarning']!=0,'CapitalChangeType']=DF2.loc[DF2['RetainedEarning']!=0,'CapitalChangeType']+'سود انباشته -'
                DF2.loc[DF2['Reserves']!=0,'CapitalChangeType']=DF2.loc[DF2['Reserves']!=0,'CapitalChangeType']+'ذخایر -'
                DF2.loc[DF2['RevaluationSurplus']!=0,'CapitalChangeType']=DF2.loc[DF2['RevaluationSurplus']!=0,'CapitalChangeType']+'تجدید ارزیابی -'
                DF2=DF2[['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl',"StockID"]]
                DF2.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl',"StockID"]
            return DF2
        else:
            time.sleep(2)
            ct=ct+1
def get_IC_N73_Stock(firm):
     ct=0
     while ct<3:
        head = {'Accept-Profile':'codalreports'}
        resp = requests.get('http://130.185.74.40:3000/View_IC_Assembly?StockID=eq.'+str(firm),headers=head)
        if resp.status_code == 200:
            DF4=pd.read_json(resp.text)
            if not DF4.empty:
                DF4['CapitalChangeType']=''
                DF4['Title']='تصمیمات مجمع عمومی فوق العاده'
                # DF2.loc[DF2['Correction'],'Title']=DF2.loc[DF2['Correction'],'Title']+['-اصلاحیه']
                DF4.loc[DF4['CashIncoming_Final']!=0,'CapitalChangeType']=DF4.loc[DF4['CashIncoming_Final']!=0,'CapitalChangeType']+'آورده -'
                DF4.loc[DF4['RetainedEarning_Final']!=0,'CapitalChangeType']=DF4.loc[DF4['RetainedEarning_Final']!=0,'CapitalChangeType']+'سود انباشته -'
                DF4.loc[DF4['Reserves_Final']!=0,'CapitalChangeType']=DF4.loc[DF4['Reserves_Final']!=0,'CapitalChangeType']+'ذخایر -'
                DF4.loc[DF4['Reevaluation_Final']!=0,'CapitalChangeType']=DF4.loc[DF4['Reevaluation_Final']!=0,'CapitalChangeType']+'تجدید ارزیابی -'
                DF4=DF4[['ticker','PublishTime','Title','IncreasePercent_Final','CapitalChangeType','HtmlUrl',"StockID"]]
                DF4.columns=['ticker','PublishTime','Title','IncreasePercent','CapitalChangeType','HtmlUrl',"StockID"]
            return DF4
        else:
            time.sleep(2)
            ct=ct+1
def get_IC_Done(firm):
    DF4=get_IC_N73_Stock(firm)
    DF2=get_IC_Assembly_Stock(firm)
    DFT=DF4.append(DF2)
    if not DFT.empty:
        DFT.sort_values(by=['PublishTime'],ascending=False)
        DFT=DFT[DFT['IncreasePercent']!=0]
    return json.loads(DFT.to_json(orient="records"))


# if __name__=="__main__":
#     #print()
    
# print(optionRequest())
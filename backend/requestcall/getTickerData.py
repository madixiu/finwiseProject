import requests
import json
import time
from .util.FixGetTechnicalIndicatorsAll import fixData 
import pandas as pd

# id = 0

dataAvailablity = False
TablesAvailability = False
names=[]
# Tables = []
parsed_json=[]
parsed_tableList = []


def getParsedData():
    head = {'Accept-Profile':'public'}
    baseUrl = 'http://130.185.74.40:3000/'
    try:
        resp = requests.get(baseUrl + 'FirmsAll',headers = head)
        if resp.status_code == 200:
            global parsed_json
            global dataAvailablity
            parsed_json = (json.loads(resp.text))
            dataAvailablity = True
        else: 
            dataAvailablity = False

        resp = requests.get(baseUrl + 'ViewsAll')
        if resp.status_code == 200:
            global parsed_tableList
            global TablesAvailability
            parsed_tableList = json.loads(resp.text)
            TablesAvailability = True
        else:
            TablesAvailability = False

    except :
        print("error connecting to main data center")
def getTickerID(tickerName):
    for ticker in parsed_json:
        if ticker['ticker'] == tickerName:
            return ticker['ID']

def getTechnicalIndicators(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'technical'}
        resp = requests.get('http://185.231.115.223:3000/View_Technical_Indicators?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ([])
def getTechnicalIndicators2(identifier):
    ct=0
    while ct<3:
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
            # DF=pd.DataFrame(json.loads(resp.text))
            # if len(DF.columns)!=0:
            #     DF=DF.transpose().reset_index()
            #     DF.columns=["title",'Value']
            #     return([json.loads(DF.to_json(orient="records")),result])
            # else:
            #     return([json.loads(DF.to_json(orient="records")),result])
        else:
            time.sleep(2)
            ct=ct+1
        
    return ([])    
def getTechnicalIndicatorsAll():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'technical'}
        resp = requests.get('http://185.231.115.223:3000/View_Technical_IndicatorsAll',headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return fixData(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")   

def getIndicesHistoric():
    ct=0
    while ct<3:
        head = {'Accept-Profile':'indices'}
        resp=requests.get('http://185.231.115.223:3000/View_HistoricIndicesReturn',headers=head)
        # resp = requests.get('http://185.231.115.223:3000/View_indices_lastMarketCap',headers=head)
        if resp.status_code == 200:
            # DF=resp.text
            # resp2 = requests.get('http://185.231.115.223:3000/View_Indices_Historic',headers=head)
            # if resp2.status_code == 200:
            #     DF2=resp2.text
            #     Indices=pd.read_json(DF)
            #     Indices['D1']=0
            #     Indices['W1']=0
            #     Indices['M1']=0
            #     Indices['M3']=0
            #     Indices['Y1']=0
            #     Indices['T']=0
            #     Indices['Name']=''
            #     Values=pd.read_json(DF2)
            #     for t in Values.CorrectName.unique().tolist():
            #         temp=Values[(Values['CorrectName']==t)&(Values['Value']!=0)]
            #         temp.sort_values(by=['englishDate'],ascending=False,inplace=True)
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'D1']=((temp.iloc[0]['Value']-temp.iloc[1]['Value'])/temp.iloc[1]['Value'])*100
            #         OneW = datetime.strftime(datetime.strptime(temp.iloc[0]['englishDate'],'%Y-%m-%d')- timedelta(days=7),'%Y-%m-%d')    
            #         OneM = datetime.strftime(datetime.strptime(temp.iloc[0]['englishDate'],'%Y-%m-%d')- timedelta(days=30),'%Y-%m-%d')
            #         ThreeM = datetime.strftime(datetime.strptime(temp.iloc[0]['englishDate'],'%Y-%m-%d')- timedelta(days=90),'%Y-%m-%d')
            #         OneY = datetime.strftime(datetime.strptime(temp.iloc[0]['englishDate'],'%Y-%m-%d')- timedelta(days=365),'%Y-%m-%d')
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'W1']=((temp[temp['englishDate']>OneW].iloc[0]['Value']-temp[temp['englishDate']>OneW].iloc[-1]['Value'])/temp[temp['englishDate']>OneW].iloc[-1]['Value'])*100
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'M1']=((temp[temp['englishDate']>OneM].iloc[0]['Value']-temp[temp['englishDate']>OneM].iloc[-1]['Value'])/temp[temp['englishDate']>OneM].iloc[-1]['Value'])*100
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'M3']=((temp[temp['englishDate']>ThreeM].iloc[0]['Value']-temp[temp['englishDate']>ThreeM].iloc[-1]['Value'])/temp[temp['englishDate']>ThreeM].iloc[-1]['Value'])*100
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'Y1']=((temp[temp['englishDate']>OneY].iloc[0]['Value']-temp[temp['englishDate']>OneY].iloc[-1]['Value'])/temp[temp['englishDate']>OneY].iloc[-1]['Value'])*100
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'T']=((temp.iloc[0]['Value']-temp.iloc[-1]['Value'])/temp.iloc[-1]['Value'])*100
            #         Indices.loc[Indices['indexID']==temp.indexID.unique().tolist()[0],'Name']=temp.iloc[0]['CorrectName']
            #     return(json.loads(pd.DataFrame.to_json(Indices,orient="index")))
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
    return ("noData")
# def getIndicesLatestCap():
#     ct=0
#     while ct<3:
#         head = {'Accept-Profile':'indices'}
#         resp = requests.get('http://185.231.115.223:3000/View_indices_lastMarketCap',headers=head)
#         if resp.status_code == 200:
#             DF=pd.esp.text)
#             # return(resp.text)
#             resp2 = requests.get('http://185.231.115.223:3000/View_Indices_Historic',headers=head)
#             if resp2.status_code == 200:
#                 print(resp2.text)
#             return (json.loads(resp.text))
#         # return(json.loads(resp.text))
#         else:
#             time.sleep(2)
#             ct=ct+1
        
#     return ("noData")    



def tickerNameRequest(): 
    ct=0
    while ct<3:
        resp = requests.get('http://130.185.74.40:3000/View_tickerOnly')
        if resp.status_code == 200:
    
            # return(resp.text)
            return (json.loads(resp.text))
        # return(json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return ("noData")

def tableNameRequest():
    Tables=[]
    if not TablesAvailability:
        getParsedData()
    if TablesAvailability:
       
        for table in parsed_tableList:
            
            Tables.append(table)
            # print(len(Tables))
            # print(parsed_tableList)
            # Tables.append(table['table_name'])
        # print(Tables)
        return(Tables)
    else:
        return ("noData")

def getDataTableHeaders(tickerName,tableName):
    
    # if id != 0:
    #     resp = requests.get('http://130.185.74.40:3000/firm', {"ID":'eq.'+})
    #     if resp.status_code == 200:
    #         return (return.text)
    # else:
    #     return ("noData")
    
    if len(parsed_json) !=0 and dataAvailablity:
        baseUrl = 'http://130.185.74.40:3000/'
        url = baseUrl + tableName+ '?firm=eq.'+ str(getTickerID(tickerName))
        print("here is URL:" + url)
        data = requests.get(url)
        parsed_data = json.loads(data.text) 
        if len(parsed_data)!=0:
                    listOFheaders=[]
                    for key in parsed_data[0].keys():
                        dict={}
                        dict['text']=key
                        dict['value']=key
                        listOFheaders.append(dict)
                    # print(listOFheaders)
                    return listOFheaders


                    
        # for ticker in parsed_json:
        #     if ticker['ticker'] == tickerName:
        #         print(ticker['ID'])
        #         url = baseUrl +tableName+ '?firm=eq.'+str(ticker['ID'])
        #         print(url)
        #         data=requests.get(url)
        #         parsed_data=json.loads(data.text)
        #         if len(parsed_data)!=0:
        #             listOFheaders=[]
        #             for key in parsed_data[0].keys():
        #                 dict={}
        #                 dict['text']=key
        #                 dict['value']=key
        #                 listOFheaders.append(dict)
        #             print(listOFheaders)
        #             return listOFheaders
    else: 
        print ('empty')


def getDataTable(tickerName ,tableName):
    baseUrl = 'http://130.185.74.40:3000/'
    url = baseUrl + tableName+ '?firm=eq.'+ str(getTickerID(tickerName))
    resp = requests.get(url)
    parsed_dataTable = json.loads(resp.text) 
    return parsed_dataTable

def getCalculatedValuationRatios(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/View_ValuationRatios?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return []
# def getCEOchange(tickerName):
#     baseUrl = 'http://130.185.74.40:3000/BoardChange_CEOChanges'
#     # if id != 0:
#     #     resp = requests.get('http://130.185.74.40:3000/firm', {"ID":'eq.'+})
#     #     if resp.status_code == 200:
#     #         return (return.text)
#     # else:
#     #     return ("noData")
#     if len(parsed_json) !=0 and dataAvailablity:
#         print(tickerName)
#         for ticker in parsed_json:
#             if ticker['ticker'] == tickerName:
#                 print(ticker['ID'])
#                 url = baseUrl + '?firm=eq.'+str(ticker['ID'])
#                 print(url)
#                 data=requests.get(url)
#                 parsed_data=json.loads(data.text)
#                 if len(parsed_data)!=0:
#                     listOFheaders=[]
#                     for key in parsed_data[0].keys():
#                         dict={}
#                         dict['text']=key
#                         dict['value']=key
#                         listOFheaders.append(dict)
#                     print(listOFheaders)
#     else: 
#         print ('empty')
def getFundamentalRatiosToDisplay(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/RatiosToDisplay?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return []
def getFundamentalLatestComponents(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'statement'}
        resp = requests.get('http://130.185.74.40:3000/View_LatestValuationComponent?firm=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return []    
def getStockHH(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'marketwatch'}
        resp = requests.get('http://185.231.115.223:3000/View_HH_Historic?ID=eq.'+str(identifier),headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return []        
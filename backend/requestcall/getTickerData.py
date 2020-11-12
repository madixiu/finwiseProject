import requests
import json


# id = 0

dataAvailablity = False
TablesAvailability = False
names=[]
# Tables = []
parsed_json=[]
parsed_tableList = []


def getParsedData():
    head = {'Accept-Profile':'public'}
    baseUrl = 'http://185.97.117.60:3000/'
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



def tickerNameRequest(): 
    # head = {'Accept-Profile':'public'}
    # resp = requests.get('http://185.97.117.60:3000/FirmsAll',headers = head)
    # if resp.status_code == 200:
    #     parsed_json = (json.loads(resp.text))
    if not dataAvailablity:
        getParsedData()
    if dataAvailablity:
        for ticker in parsed_json:
            names.append(ticker['ticker'])
        return (names)
    # maybe this is redundant
    else:
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
    #     resp = requests.get('http://185.97.117.60:3000/firm', {"ID":'eq.'+})
    #     if resp.status_code == 200:
    #         return (return.text)
    # else:
    #     return ("noData")
    
    if len(parsed_json) !=0 and dataAvailablity:
        baseUrl = 'http://185.97.117.60:3000/'
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
    baseUrl = 'http://185.97.117.60:3000/'
    url = baseUrl + tableName+ '?firm=eq.'+ str(getTickerID(tickerName))
    resp = requests.get(url)
    parsed_dataTable = json.loads(resp.text) 
    return parsed_dataTable


# def getCEOchange(tickerName):
#     baseUrl = 'http://185.97.117.60:3000/BoardChange_CEOChanges'
#     # if id != 0:
#     #     resp = requests.get('http://185.97.117.60:3000/firm', {"ID":'eq.'+})
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
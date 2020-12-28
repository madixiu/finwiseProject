import requests
import json
from .util.dataAlterTest import listCreator
from .util.Convereter_trunc import truncater

# this is Market table headers
# MarketTableHeader = [
# {'label': 'fuck', 'field':'fuck'},
# {'label': 'نماد', 'field': 'ticker'}, 
# {'label': 'نام', 'field': 'name'}, 
# {'label': 'صنعت', 'field': 'industry'},
# {'label': 'بازار', 'field': 'marketName'},
# {'label': 'آخرین بروز رسانی', 'field': 'updatedAt'}, 
# # {'label': 'مبنا', 'field': 'Mabna'}, 
# {'label': 'کف مجاز قیمت', 'field': 'MinRange'}, 
# {'label': 'سقف مجاز قیمت', 'field': 'MaxRange'}, 
# {'label': 'EPS', 'field': 'EPS'},
# {'label': 'حجم معاملات', 'field': 'TradeVolume'},
# {'label': 'ارزش معاملات', 'field': 'TradeValue'},
# {'label': 'تعداد معاملات', 'field': 'TradeCount'},
# {'label': 'قیمت دیروز', 'field': 'yesterday'}, 
# {'label': 'بالاترین قیمت', 'field': 'high'}, 
# {'label': 'کمترین قیمت', 'field': 'low'},
# {'label': 'آخرین قیمت', 'field': 'last'}, 
# {'label': 'قیمت پایانی', 'field': 'close'},
# {'label': 'اولین قیمت', 'field': 'first'},

# {'label': 'تعداد خرید حقیقی', 'field': 'CountBuy_Haghighi'}, 
# {'label': 'تعداد خرید حقوقی', 'field': 'CountBuy_Hoguhgi'},
# {'label': 'حجم خرید حقیقی', 'field': 'VolumeBuy_Haghighi'}, 
# {'label': 'حجم خرید حقوقی', 'field': 'VolumeBuy_Hoghughi'}, 
# {'label': 'تعداد فروش حقیقی', 'field': 'CountSell_Haghighi'}, 
# {'label': 'تعداد فروش حقوقی', 'field': 'CountSell_Hoghughi'}, 
# {'label': 'حجم فروش حقیقی', 'field': 'VolumeSell_Haghighi'}, 
# {'label': 'حجم فروش حقوقی', 'field': 'VolumeSell_Hoghughi'}
# ]

dataAvailablity = False
filterAvailability = False
parsed_data = []

ListOfFilterTypes = []
ListOfFilterIndustry = []

def getParsedData():
    
    try:
        # resp = requests.get('http://37.152.180.99:3000/ViewWatch', headers = head)
        resp = requests.get('http://37.152.180.99:3000/ViewWatch')
        if resp.status_code == 200:
            if resp.text:
                global parsed_data
                global dataAvailablity
                parsed_data = []
                parsed_data = json.loads(resp.text)
                dataAvailablity = True
                additionalDataMarketWatch()
    except:
        print("connection could not be established to data center!")

def getFilteredData(marketName,marketType,marketIndustry):
    # dataTemp = []
    getParsedData()
    if marketType==[]:
        if marketName=='همه':
            if marketIndustry==[]:
                dataTemp = parsed_data
            else:
                dataTemp =[x for x in parsed_data if (x['industry'] in marketIndustry)]
        else:
            if marketIndustry==[]:
                # print('here')
                if marketName =="بورس":
                    dataTemp = [x for x in parsed_data if x["marketParent"] == 1]
                    # 
                else:
                    dataTemp = [x for x in parsed_data if x["marketParent"] == 2 or x["marketParent"] == 20]
                # print(dataTemp)
            else: 
                if marketName == "بورس":
                    dataTemp=[x for x in parsed_data if x["marketParent"]==1 and x['industry'] in marketIndustry]
                else:
                    dataTemp=[x for x in parsed_data if (x["marketParent"]==2 or x['marketParent'] == 20) and x['industry'] in marketIndustry]

    else:
        if marketName=='همه':
            if marketIndustry==[]:
                dataTemp=[x for x in parsed_data if x["Type"] in marketType ]
            else:
                dataTemp=[x for x in parsed_data if x["Type"] in marketType and x['industry'] in marketIndustry]
        else:
            if marketIndustry==[]:
                if marketName == "بورس":
                    dataTemp=[x for x in parsed_data if x["Type"] in marketType and x["marketParent"]== 1]
                else:
                    dataTemp=[x for x in parsed_data if x["Type"] in marketType and x["marketParent"]== 2 or x["marketParent"] == 20]
            else:
                if marketName == "بورس":
                    dataTemp=[x for x in parsed_data if (x["Type"] in marketType and x["marketParent"]==1) and x['industry'] in marketIndustry]
                else:
                    dataTemp=[x for x in parsed_data if x["Type"] in marketType and (x["marketParent"]==2 or x["marketParent"]==20) and x['industry'] in marketIndustry]

    
    return dataTemp
    # dataTemp = []
    # temp =[]
    # if marketName != 'all':
    #     for item in parsed_data:
    #         if marketName != 'all' :
    #             if marketName == 'بورس':
    #                 if item["marketParent"] == 1:
    #                     temp.append(item)
    #             if marketName == 'فرابورس':
    #                 if item["marketParent"] == 2 or item["marketParent"] == 20:
    #                     temp.append(item)
    #     dataTemp = temp
    #     print(len(dataTemp))
    #     print(marketType)
    #     # temp =[]    
    # else:
    #     dataTemp = parsed_data
    #     # dataTemp = parsed_data
    #     # temp = []
    # count = 0
    # for Finalitem in dataTemp:
    #     temp = []
    #     # count+=1
    #     if marketType != [] and marketIndustry != []:
    #         if Finalitem["Type"] in marketType and Finalitem["industry"] in marketIndustry:
    #             temp.append(Finalitem)
    #     if marketType != [] and marketIndustry == []:
            
    #         if  Finalitem["Type"] in marketType:
    #             # dataTemp.remove(Finalitem)
    #             temp.append(Finalitem)
    #             print(temp)
    #             # print(len(marketType))
    #             # break
    #     if marketIndustry != [] and marketType == []:
    #         if Finalitem["industry"] in marketIndustry:
    #             temp.append(Finalitem)
    # print (count)
    # return temp
        

def getMarketWatchRequest():
    getParsedData()
    if dataAvailablity:
        # DataAlterTesting()
        # additionalDataMarketWatch()
        return (parsed_data)
    else:
        return ("noData")

# def getMarketWatchHeaderReq():
#         return (MarketTableHeader)
    # except :
    #     print("there seems to be error in returning Market Watch header")
    #     return ("noData")
    # columns = []
    #
    # if dataAvailablity:
        
        # old way to get headers (depriciated) [this is a comment]
        # dict_keys = list(parsed_data[0].keys())
        # for i in dict_keys:
        #     myDict = {}
        #     myDict["label"] = i
        #     myDict["field"] = i
        #     columns.append(myDict)
        # return (MarketTableHeader)
    # else:
        # return("noData")
def filterListFill():
    filters=[]
    for i in parsed_data:
        if i["Type"] not in ListOfFilterTypes and i["Type"] != None :
            ListOfFilterTypes.append(i["Type"]) 
        if i["industry"] not in ListOfFilterIndustry and i["industry"] != None:
            ListOfFilterIndustry.append(i["industry"])
    filters.append(ListOfFilterTypes)
    filters.append(ListOfFilterIndustry)
    return filters

def getMarketWatchFilterLists():
    if dataAvailablity and parsed_data and not filterAvailability:
        return filterListFill()
    elif  not dataAvailablity and not filterAvailability: 
        getParsedData()
        return filterListFill()
    else:
        # print(dataAvailablity)
        return "noData"
    

def DataAlterTesting():
    lst = []
    lst = listCreator(len(parsed_data))
    i = 0
    for item in parsed_data:
        item['test'] = lst[i]
        i+=1

def additionalDataMarketWatch():
    for item in parsed_data:
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None
    print(parsed_data[0])
    
from django.http import HttpResponse,JsonResponse
import json
import requests
from rest_framework.parsers import JSONParser 
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from requestcall.getOptions import optionRequest
from requestcall.getTickerData import getDataTable, getDataTableHeaders, tickerNameRequest,tableNameRequest
# from requestcall.getMarketWatch import  getMarketWatchRequest,getMarketWatchFilterLists, getFilteredData
from requestcall.getMarketWatch2 import  getMarketWatchRequest,getMarketWatchFilterLists,getFilteredData
from requestcall.getCodalNotices import *
from requestcall.getTseData import *
from requestcall.getIndexMarketCap import IndexMarketCapRequest
from requestcall.getViewOptionAssetVolatility import OptionAssetVolatility
from requestcall.getTickerTapeData import TickerTapeData
from requestcall.getAssemblyData import firstStepAssembly,secondStepAssembly
from requestcall.getSearchData import SearchData
from requestcall.treeMapData import getMapData
from requestcall.getMainAssemblyData import AssemblyListData,getCalendarData
from requestcall.getOragh_HaghTaghadom_FundsData import getOraghData,getHaghTaghadomData,getFundsData
from requestcall.getTVData import ListOfStocks

def getCodalNoticesAll(self,identifier):
    return JsonResponse(CodalNoticesRequest(identifier),safe=False)
def getSubHeader(self,identifier):
    return JsonResponse(SubHeader(identifier),safe=False)   
def getHHhistory(self,identifier):
    return JsonResponse(HHhistory(identifier),safe=False)
def getAdjustedPriceHistory(self,identifier):
    return JsonResponse(AdjustedPrices(identifier),safe=False)
def getCurrentBoard(self,identifier):
    return JsonResponse(getBoard(identifier),safe=False)
def getCurrentCeo(self,identifier):
    return JsonResponse(getceo(identifier),safe=False)
def getStatusChanges(self,identifier):
    return JsonResponse(StatusChanges(identifier),safe=False)    
def getAdminNotice(self,firm):
    return JsonResponse(getAdminsNotices(firm),safe=False)    
def getStatsTicker(self,identifier):
    return JsonResponse(getStatisticsTicker(identifier),safe=False)
def getLiveTicker(self,identifier):
    return JsonResponse(getLive_ticker(identifier),safe=False)
def getLiveHHTicker(self,identifier):
    return JsonResponse(getLiveHHtickerData(identifier),safe=False)
def getAllDPS(self,identifier):
    return JsonResponse(getAllDps(identifier),safe=False)    
def getAdminNotices(self,identifier):
    return JsonResponse(get_AdminsNotice(identifier),safe=False)    
######TSE
def getTop5MostViewed(self):
    return JsonResponse(Top5MostViewed(),safe=False)    

###MonthlyBeginsHere
def getTypeOfMonthly(self,identifier):
    return JsonResponse(getTypeOffirm(identifier),safe=False)
def getMonthlyBank_Deposits(self,identifier):
    return JsonResponse(monthlyBankDeposits(identifier),safe=False)
def getMonthlyBank_Facility(self,identifier):
    return JsonResponse(monthlyBankFacility(identifier),safe=False)
def getMonthlyInsurance(self,identifier):
    return JsonResponse(monthlyInsurance(identifier),safe=False)
def getMonthlyConstSold(self,identifier):
    return JsonResponse(monthlyConstSold(identifier),safe=False)    
def getMonthlyConstOngoing(self,identifier):
    return JsonResponse(monthlyConstOngoing(identifier),safe=False)  
def getMonthlyProduction(self,identifier):
    return JsonResponse(monthlyProduction(identifier),safe=False)

def getMonthlyInvestment_InTrans(self,identifier):
    return JsonResponse(monthlyInvestInTransactions(identifier),safe=False)
def getMonthlyInvestment_OutTrans(self,identifier):
    return JsonResponse(monthlyInvestOutTransactions(identifier),safe=False)
def getMonthlyInvestment_Portfo(self,identifier):
    return JsonResponse(monthlyInvestPortf(identifier),safe=False)
def getMonthlyInvestment_Summary(self,identifier):
    return JsonResponse(monthlyInvestSummary(identifier),safe=False)
def getShareHolders(self,identifier):
    return JsonResponse(getShareholdersList(identifier),safe=False)
def getBalanceSheetAll(self,identifier):
    return JsonResponse(getBalanceSheetFirm(identifier),safe=False)


##############Monthly Ends Here





def getIndexMarketCap(self):
    return JsonResponse(IndexMarketCapRequest(),safe=False)  

def getOptions(self):
    # if(optionFlag()):
        return JsonResponse(optionRequest(),safe=False)
    # else:
    #     return HttpResponse("noData")

def getTickersNames(self):
    return JsonResponse(tickerNameRequest(),safe=False)

def getTableNames(self):
    return JsonResponse(tableNameRequest(),safe=False)

@csrf_exempt
def findTickerID(request):
    if request.method == 'POST':
        response=[]
        data = JSONParser().parse(request)
        # getCEOchange(data.get('title'))
        # print('this is the data django recieved' +data.get('tickerName') + 'and this table : ' + data.get('selectedTable'))
        response.append(getDataTableHeaders(data.get('tickerName'),data.get('selectedTable')))
        response.append(getDataTable(data.get('tickerName'),data.get('selectedTable')))
        # return HttpResponse("OK")
        return JsonResponse(response,safe=False)

def getMarketWatchFilterOptions(request):
    pass
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
        # response = 
## OLD MARKETWATCH VIEW ************************************************************************************************
# @csrf_exempt
# def getMarketWatch(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         if data.get('marketName') != "همه" or data.get('marketType') != [] or data.get('marketIndustry') != []:
#             respond = getFilteredData(data.get('marketName'),data.get('marketType'),data.get('marketIndustry'))
#         else: 
#             respond = getMarketWatchRequest()
#         return HttpResponse(json.dumps(respond))
#     if request.method == 'GET':
#         return HttpResponse(json.dumps(getMarketWatchRequest()))
## OLD MARKETWATCH VIEW *************************************************************************************************

@csrf_exempt
def getMarketWatch(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(len(getFilteredData(data.get("marketName"),data.get('marketIndustry'))))
        return JsonResponse(getFilteredData(data.get("marketName"),data.get('marketIndustry')),safe=False)
    if request.method == 'GET':
        return JsonResponse(getMarketWatchRequest(),safe=False)

def getMarketWatchFilters(self):
    return JsonResponse(getMarketWatchFilterLists(),safe=False)


def getOptionAssets(self):
    return JsonResponse(OptionAssetVolatility(),safe=False)


def getTape(self):
    return JsonResponse(TickerTapeData(),safe=False)

# def get_csrf_token(request):
#     token = django.middleware.csrf.get_token(request)
#     return JsonResponse({'token': token})

@csrf_exempt
def getAssembly(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(data)
        return JsonResponse(firstStepAssembly(data), safe=False)

@csrf_exempt
def getAssemblyDetails(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return JsonResponse(secondStepAssembly(data.get('SummaryID'),data.get('Type')), safe=False)
    # if request.method == 'GET':
    #     # data = JSONParser().parse(request)
    #     return JsonResponse(secondStepAssembly(), safe=False)

def getSearchBarData(self):
    return JsonResponse(SearchData(),safe=False)

def getMarketMap(self):
    return JsonResponse(getMapData(),safe=False)

def getMainAssembly(self):
    return JsonResponse(AssemblyListData(),safe=False)
def getMainCalendar(self):
    return JsonResponse(getCalendarData(),safe=False)

def getHaghTaghadom(self):
    return JsonResponse(getHaghTaghadomData(),safe=False)
def getOragh(self):
    return JsonResponse(getOraghData(),safe=False)
def getFunds(self):
    return JsonResponse(getFundsData(),safe=False)

def getTradingViewData(self):
    return JsonResponse(ListOfStocks(),safe=False)
####################################################


def getHighestValue(self):
        return JsonResponse(highestTvalues(),safe=False)
def getLatestNews(self):
        return JsonResponse(getNews(),safe=False)

def getTVHHTotal(self):
        return JsonResponse(TradeValueHH(),safe=False)
def getTVHHAsset(self):
        return JsonResponse(TradeValueHHBasedOnAsset(),safe=False)
        
def getTVAssets(self):
        return JsonResponse(TradeValueAsset(),safe=False)
def getIFBTEPIX(self):
        return JsonResponse(getLatestTwoIndex(),safe=False)                        
def getTodayTepix(self):
    return JsonResponse(getLastActiveDayTepix(),safe=False)                        
def getAllTradesValue(self):
    return JsonResponse([TradeValueHH(),TradeValueHHBasedOnAsset(),TradeValueAsset(),getLatestTwoIndex()],safe=False)

###################################################
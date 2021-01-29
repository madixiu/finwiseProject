from django.http import HttpResponse,JsonResponse
import json
import requests
from rest_framework.parsers import JSONParser 
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from requestcall.getOptions import optionRequest
from requestcall.getTickerData import getDataTable, getDataTableHeaders, tickerNameRequest,tableNameRequest
from requestcall.getMarketWatch import  getMarketWatchRequest,getMarketWatchFilterLists, getFilteredData
from requestcall.getCodalNotices import *
from requestcall.getTseData import *
from requestcall.getIndexMarketCap import IndexMarketCapRequest
from requestcall.getViewOptionAssetVolatility import OptionAssetVolatility
from requestcall.getTickerTapeData import TickerTapeData
from requestcall.getAssemblyData import firstStepAssembly,secondStepAssembly
from requestcall.getSearchData import SearchData
from requestcall.treeMapData import getMapData
from requestcall.getMainAssemblyData import AssemblyListData,getCalendarData
# from requestcall.getTVData import 

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
def getAllDPS(self,identifier):
    return JsonResponse(getAllDps(identifier),safe=False)    
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
@csrf_exempt
def getMarketWatch(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
    #    print('this is the fucking data' + data.get('marketName') + 'and '+ data.get('marketType') + 'and '+data.get('marketIndustry'))
        # print(data.get('marketName'))
        # respond.append(getMarketWatchHeaderReq())
        if data.get('marketName') != "همه" or data.get('marketType') != [] or data.get('marketIndustry') != []:
            # respond.append(getFilteredData(data.get('marketName'),data.get('marketType'),data.get('marketIndustry')))
            respond = getFilteredData(data.get('marketName'),data.get('marketType'),data.get('marketIndustry'))
        else: 
            # respond.append(getMarketWatchRequest())
            respond = getMarketWatchRequest()
        # return JsonResponse(respond,safe=False)
        return HttpResponse(json.dumps(respond))
    if request.method == 'GET':
        # resp = []
        # resp.append(getMarketWatchHeaderReq())
        # resp.append(getMarketWatchRequest())
        # return JsonResponse(resp,safe=False)
        return HttpResponse(json.dumps(getMarketWatchRequest()))
        # return JsonResponse(getMarketWatchRequest(),safe=False)


def getMarketWatchFilters(self):
    # resp = []
    # resp.append(getMarketWatchFilterLists)
    # print(getMarketWatchFilterLists())
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
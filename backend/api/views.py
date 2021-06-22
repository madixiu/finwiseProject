from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_control
from users.models import CustomUser

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from graphql_jwt.decorators import login_required
from graphql_jwt.utils import jwt_decode

from rest_framework.parsers import JSONParser 
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from requestcall.getOptions import optionRequest
from requestcall.getTickerData import *
# from requestcall.getMarketWatch import  getMarketWatchRequest,getMarketWatchFilterLists, getFilteredData
from requestcall.getMarketWatch2 import  getMarketWatchRequest,getMarketWatchFilterLists,getFilteredData
from requestcall.getCodalNotices import *
from requestcall.getTseData import *
from requestcall.getCommodities import *
from requestcall.getCryptoData import *
from requestcall.getIndexMarketCap import IndexMarketCapRequest
from requestcall.getViewOptionAssetVolatility import OptionAssetVolatility
from requestcall.getTickerTapeData import TickerTapeData,IndustryTapeData
from requestcall.getAssemblyData import firstStepAssembly,secondStepAssembly
from requestcall.getSearchData import SearchData
from requestcall.treeMapData import getMapData
from requestcall.getMainAssemblyData import AssemblyListData,getCalendarData
from requestcall.getOragh_HaghTaghadom_FundsData import getOraghData,getHaghTaghadomData,getFundsData,getCryptoMarketData
from requestcall.getTVData import TVtickerData

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
def getIndexDetails(self,identifier):
    return JsonResponse(getIndicesDetails(identifier),safe=False)
def getIndicesHH(self):
    return JsonResponse(AllIndicesHH(),safe=False)
def getIndicesImpact(self):
    return JsonResponse(AllIndicesImpact(),safe=False)
def getAllIndustriesData(self):
    return JsonResponse([getIndicesHistoric(),IndexMarketCapRequest(),AllIndicesHH(),AllIndicesImpact()],safe=False)



def getLastestIC(self):
    return JsonResponse(get_IC_ALL(),safe=False)
def getLastestICDone(self,identifier):
    return JsonResponse(get_IC_Done(identifier),safe=False)
def getAllDashboard(self):
    return JsonResponse([ImpactOnIndex(),highestTvalues(),
    [TradeValueHH(),TradeValueHHBasedOnAsset(),TradeValueAsset(),getLatestTwoIndex()],getNews(),getMarketHH(),[highestSupplies(),highestDemands()]
    ,getLastActiveDayTepix(),getTechnicalIndicatorsAll()],safe=False)

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
def getMonthlyProductionAnalysis1(self,identifier):
    return JsonResponse(monthlyPAnalysis1(identifier),safe=False)    
def getMonthlyServices(self,identifier):
    return JsonResponse(monthlyService(identifier),safe=False)
def getMonthlyLeasingCost(self,identifier):
    return JsonResponse(monthly_leasing_cost(identifier),safe=False)
def getMonthlyLeasingDelegated(self,identifier):
    return JsonResponse(monthly_leasing_delegated(identifier),safe=False)
def getMonthlyLeasingRevenue(self,identifier):
    return JsonResponse(monthly_leasing_revenue(identifier),safe=False)
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
def getIncomeStatementAll(self,identifier):
    return JsonResponse(getIncomeStatementFirm(identifier),safe=False)
def getCFAll(self,identifier):
    return JsonResponse(getCFFirm(identifier),safe=False)

##############Monthly Ends Here
def getIndicators(self,identifier):
    return JsonResponse(getTechnicalIndicators(identifier),safe=False)
def getIndicators2(self,identifier):
    return JsonResponse(getTechnicalIndicators2(identifier),safe=False)    
def getIndicatorsAll(self):
    return JsonResponse(getTechnicalIndicatorsAll(),safe=False)
def getHistoricCap(self):
    return JsonResponse(getIndicesHistoric(),safe=False)

######### crypto
def getAllCryptoTechnical(self):
    return JsonResponse(getCryptoTechnicalIndicators(),safe=False)
def getCryptoCorr(self):
    return JsonResponse(getCryptoCorrelation(),safe=False)
def getIndicatorsCrypto(self,identifier):
    return JsonResponse(getSingleCryptoTechnical(identifier),safe=False)
def getCyptoMWIntro(self):
    return JsonResponse(getBCMarketWatch(),safe=False)
def getCyptoMWAll(self):
    return JsonResponse(getBCMarketWatchAll(),safe=False)
def getBasicCrypto(self,identifier):
    return JsonResponse(getBasicCryptoData(identifier),safe=False)
def getCryptoLive(self,identifier):
    return JsonResponse(getSingleCryptoLive(identifier),safe=False)
def getIndexMarketCap(self):
    return JsonResponse(IndexMarketCapRequest(),safe=False)  

############### OPTOIN ###############
# @permission_classes([IsAuthenticated,])
# @login_required
# @permission_classes([IsAuthenticated])
# @permission_classes(IsAuthenticated, )
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getOptions(request):
    tokenA = request.META.get('HTTP_AUTHORIZATION')[7:]
    try:
        payload = jwt_decode(tokenA)
        username = payload["username"]
        user = CustomUser.objects.get(username = username)
        # print(user)
        # role = user.role
        if user.role >= 2:
            return JsonResponse(optionRequest(),safe=False)
        else:
            return JsonResponse("AccessDenied")
        # return JsonResponse(role,safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)


    # return JsonResponse(optionRequest(),safe=False)
def getOptionAssets(self):
    return JsonResponse(OptionAssetVolatility(),safe=False)
############### OPTOIN ###############


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


############### MARKET WATCH ###############

@csrf_exempt
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getMarketWatch(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(len(getFilteredData(data.get("marketName"),data.get('marketIndustry'))))
        return JsonResponse(getFilteredData(data.get("marketName"),data.get('marketIndustry')),safe=False)
    if request.method == 'GET':
        return JsonResponse(getMarketWatchRequest(),safe=False)

def getMarketWatchFilters(self):
    return JsonResponse(getMarketWatchFilterLists(),safe=False)
############### MARKET WATCH ###############



############### TICKER TAPE ###############

def getTape(self):
    return JsonResponse([TickerTapeData(),IndustryTapeData()],safe=False)
############### TICKER TAPE ###############

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


############### SEARCH BAR DATA ###############
def getSearchBarData(self):
    return JsonResponse(SearchData(),safe=False)
############### SEARCH BAR DATA ###############

############### MARKET MAP ###############
def getMarketMap(self):
    return JsonResponse(getMapData(),safe=False)
############### MARKET MAP ###############



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
def getCrypto(self):
    return JsonResponse(getCryptoMarketData(),safe=False)


###############TRADING VIEW#########################

def getTradingViewData(self,limits,url,todate):
    return JsonResponse(TVtickerData(limits,url,todate),safe=False)
####################################################





                      


###################################################
############### DASHBOARD #########################


def getImpactOnIndex(self):
    return JsonResponse(ImpactOnIndex(),safe=False)

def getHighestValue(self):
        return JsonResponse(highestTvalues(),safe=False)

## ASSET TRADE VALUE ##
def getTVHHTotal(self):
        return JsonResponse(TradeValueHH(),safe=False)
def getTVHHAsset(self):
        return JsonResponse(TradeValueHHBasedOnAsset(),safe=False)
        
def getTVAssets(self):
        return JsonResponse(TradeValueAsset(),safe=False)
def getIFBTEPIX(self):
        return JsonResponse(getLatestTwoIndex(),safe=False)  
## ASSET TRADE VALUE ##

## NEWS
def getLatestNews(self):
        return JsonResponse(getNews(),safe=False)

def getHHMarket(self):
    return JsonResponse(getMarketHH(),safe=False)

def getHighestSupplies(self):
    return JsonResponse(highestSupplies(),safe=False)
def getHighestDemands(self):
    return JsonResponse(highestDemands(),safe=False)

def getHighestQ(self):
    return JsonResponse([highestSupplies(),highestDemands()],safe=False)


def getTodayTepix(self):
    return JsonResponse(getLastActiveDayTepix(),safe=False)                        
def getAllTradesValue(self):
    return JsonResponse([TradeValueHH(),TradeValueHHBasedOnAsset(),TradeValueAsset(),getLatestTwoIndex()],safe=False)

# def TechnicalIndicatorAll():
#     return JsonResponse(getTechnicalIndicatorsAll(), safe=False)


######### Commodity
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesBasic(self):
    return JsonResponse(getbasicCommodityIR(),safe=False) 

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesBasicInvesting(self):
    return JsonResponse(getbasicInvesting(),safe=False) 

def getCommoditiesPetro(self):
    return JsonResponse(getPetroCommodity(),safe=False)

def getCommoditiesMB(self):
    return JsonResponse(getMBcommodity(),safe=False)

def getCommoditiesDetailIR(self,identifier):
    return JsonResponse(getHistoricIR(identifier),safe=False)

def getCommoditiesDetailInvesting(self,identifier):
    return JsonResponse(getHistoricInvesting(identifier),safe=False)
def getCommoditiesDetailPlats(self,identifier):
    return JsonResponse(getHistoricPlats(identifier),safe=False)    

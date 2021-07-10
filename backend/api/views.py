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
from requestcall.getFundsData import *
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



def CheckRole(token,role):
    try:
        payload = jwt_decode(token=token)
        username = payload["username"]
        user = CustomUser.objects.get(username = username)
      
        if user.role >= role:
            return "ok"
        else:
            return "AccessDenied"
    except:
        return "notAuthorized"
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
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getTypeOfMonthly(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getTypeOffirm(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyBank_Deposits(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyBankDeposits(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyBank_Facility(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyBankFacility(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyInsurance(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyInsurance(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyConstSold(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyConstSold(identifier),safe=False)    
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyConstOngoing(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyConstOngoing(identifier),safe=False)  
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyProduction(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyProduction(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyProductionAnalysis1(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyPAnalysis1(identifier),safe=False)    
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyServices(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyService(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyLeasingCost(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthly_leasing_cost(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyLeasingDelegated(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthly_leasing_delegated(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyLeasingRevenue(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthly_leasing_revenue(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyInvestment_InTrans(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyInvestInTransactions(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyInvestment_OutTrans(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyInvestOutTransactions(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyInvestment_Portfo(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyInvestPortf(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getMonthlyInvestment_Summary(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(monthlyInvestSummary(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getShareHolders(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getShareholdersList(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getBalanceSheetAll(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=3:
    #         return JsonResponse(getBalanceSheetFirm(identifier),safe=False)
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
    return JsonResponse(getBalanceSheetFirm(identifier),safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getBalanceSheetAllAggregated(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=3:
    #         return JsonResponse(getBalanceSheetAggregatedFirm(identifier),safe=False)
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
    return JsonResponse(getBalanceSheetAggregatedFirm(identifier),safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getIncomeStatementAll(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=3:
    #         return JsonResponse(getIncomeStatementFirm(identifier),safe=False)
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
    return JsonResponse(getIncomeStatementFirm(identifier),safe=False)

# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getIncomeStatementAllAggregated(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=3:
    #         return JsonResponse(getIncomeStatementFirm(identifier),safe=False)
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
    return JsonResponse(getIncomeStatementFirmAggrregated(identifier),safe=False)

        
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCFAll(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getCFFirm(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    

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
    if CheckRole(tokenA,2) == "ok":
        return JsonResponse(optionRequest(),safe=False)
    else:
        return JsonResponse(CheckRole(tokenA,2),safe=False)


    # try:
    #     payload = jwt_decode(tokenA)
    #     username = payload["username"]
    #     user = CustomUser.objects.get(username = username)
      
    #     if user.role >= 2:
    #         return JsonResponse(optionRequest(),safe=False)
    #     else:
    #         return JsonResponse("AccessDenied")
    # except:
    #     return JsonResponse("notAuthorized",safe=False)


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

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getImpactOnIndex(self):
    return JsonResponse(ImpactOnIndex(),safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
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

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getHHMarket(self):
    return JsonResponse(getMarketHH(),safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getHighestSupplies(self):
    return JsonResponse(highestSupplies(),safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getHighestDemands(self):
    return JsonResponse(highestDemands(),safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getHighestQ(self):
    return JsonResponse([highestSupplies(),highestDemands()],safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getTodayTepix(self):
    return JsonResponse(getLastActiveDayTepix(),safe=False)

@cache_control(max_age=50, no_cache=True, no_store=True, must_revalidate=True)
def getAllTradesValue(self):
    return JsonResponse([TradeValueHH(),TradeValueHHBasedOnAsset(),TradeValueAsset(),getLatestTwoIndex()],safe=False)

# def TechnicalIndicatorAll():
#     return JsonResponse(getTechnicalIndicatorsAll(), safe=False)


######### Commodity
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesBasic(request):
    tokenA = request.META.get('HTTP_AUTHORIZATION')[7:]
    try:
        payload = jwt_decode(tokenA)
        username = payload["username"]
        user = CustomUser.objects.get(username = username)
        # print(user)
        # role = user.role
        if user.role >= 2:
            return JsonResponse(getbasicCommodityIR(),safe=False) 
        else:
            return JsonResponse("AccessDenied")
        # return JsonResponse(role,safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)

    # return JsonResponse(getbasicCommodityIR(),safe=False) 

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesBasicInvesting(request):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getbasicInvesting(),safe=False) 
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesPetro(request):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getPetroCommodity(),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesMB(request):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=3:
            return JsonResponse(getMBcommodity(),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesDetailIR(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=4:
            return JsonResponse(getHistoricIR(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def getCommoditiesDetailInvesting(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=4:
            return JsonResponse(getHistoricInvesting(identifier),safe=False)
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getCommoditiesDetailPlats(request,identifier):
    try:
        payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
        username=payload['username']
        user=CustomUser.objects.get(username=username)
        if user.role>=4:
            return JsonResponse(getHistoricPlats(identifier),safe=False)    
        else:
            return JsonResponse("AccessDenied",safe=False)
    except:
        return JsonResponse("notAuthorized",safe=False)
    


##########
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getFundsMeta(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=4:
            return JsonResponse(getFundsMetaData(identifier),safe=False)    
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)    
def getFundsAssetComp(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=4:
            return JsonResponse(getFundsAssetComposition(identifier),safe=False)    
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)            
def getFundsIndustryComp(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=4:
            return JsonResponse(getFundsIndustryComposition(identifier),safe=False)    
    #     else:
    #         return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)
# @cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)            
def getFundsHistoricalNav(request,identifier):
    # try:
    #     payload=jwt_decode(request.META.get('HTTP_AUTHORIZATION')[7:])
    #     username=payload['username']
    #     user=CustomUser.objects.get(username=username)
    #     if user.role>=4:
            return JsonResponse(getFundsHistoricalNavData(identifier),safe=False)    
        # else:
        #     return JsonResponse("AccessDenied",safe=False)
    # except:
    #     return JsonResponse("notAuthorized",safe=False)

from django.urls import path,re_path
from .views import *


urlpatterns = [
   # re_path(r'^get-token/$', get_csrf_token),
   path("options", getOptions),
   path("tickerallnames",getTickersNames),
   path("tableallnames",getTableNames),
   path("findTickerid",findTickerID),
   path("marketwatch",getMarketWatch),
   path("marketwatchfilterlists",getMarketWatchFilters),
   path("TradeValue/HH/Total",getTVHHTotal),
   path("TradeValue/HH/Asset",getTVHHAsset),
   path("TradeValue/Asset",getTVAssets),
   path("LatestTepixIFB",getIFBTEPIX),
   path("getAllTradesValue",getAllTradesValue),
   ######
   path("tse/getHighestValue/",getHighestValue),
   ######
   path("CodalNotices",getCodalNoticesAll),
   path("CodalNotices/<identifier>/",getCodalNoticesAll),
   path("SubHeaderW/<identifier>/",getSubHeader),
   path("HHhistoryGraph/<identifier>/",getHHhistory),
   path("AdjustedPrices/<identifier>/",getAdjustedPriceHistory),
   path("StatsTicker/<identifier>/",getStatsTicker),
   path("LiveHHTicker/<identifier>/",getLiveHHTicker),
   path("LiveTicker/<identifier>/",getLiveTicker),
   path("Alldps/<identifier>/",getAllDPS),
   path("AdminNotice/<identifier>/",getAdminNotices),
   ####Monthly
   path("Monthly/Type/<identifier>/",getTypeOfMonthly),
   path("Monthly/Bank/Deposits/<identifier>/",getMonthlyBank_Deposits),
   path("Monthly/Bank/Facilities/<identifier>/",getMonthlyBank_Facility),
   path("Monthly/Insurance/<identifier>/",getMonthlyInsurance),
   path("Monthly/Construction/Ongoing/<identifier>/",getMonthlyConstOngoing),
   path("Monthly/Construction/Sold/<identifier>/",getMonthlyConstSold),
   path("Monthly/Production/<identifier>/",getMonthlyProduction),

   path("Monthly/Investment/InTransactions/<identifier>/",getMonthlyInvestment_InTrans),
   path("Monthly/Investment/OutTransactions/<identifier>/",getMonthlyInvestment_OutTrans),
   path("Monthly/Investment/Portfolio/<identifier>/",getMonthlyInvestment_Portfo),
   path("Monthly/Investment/Summary/<identifier>/",getMonthlyInvestment_Summary),
   path("Statement/BalanceSheet/<identifier>/",getBalanceSheetAll),
############

   path("CurrentBoard/<identifier>/",getCurrentBoard),
   path("CurrentCeo/<identifier>/",getCurrentCeo),
   path("AdminNotices/<firm>/",getAdminNotice),
   path("StatusChanges/<identifier>/",getStatusChanges),
   path("Shareholders/<identifier>/",getShareHolders),
   ####
   path("IndexMarketCap",getIndexMarketCap),
   path("ViewOptionAssetVolatility",getOptionAssets),
   path("TickerTape",getTape),
   ## Ticker Assembly
   path("tickerAssemblyStepOne",getAssembly),
   path("tickerAssemblyStepTwo",getAssemblyDetails),
   ## Main Assembly
   path("MainAssemblyDataList",getMainAssembly),
   path("MainCalendar",getMainCalendar),
   ##
   path("MainSearchBar",getSearchBarData),
   ###
   path("Map",getMarketMap),
   path("TVData",getTradingViewData),

   ###
   path("HaghTaghadom",getHaghTaghadom),
   path("Oragh",getOragh),
   path("Funds",getFunds)

]

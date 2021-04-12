
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
   path("getTodayTepix",getTodayTepix),
   path("LatestNews",getLatestNews),
   path("LatestIC",getLastestIC),
   path("LatestICDone/<identifier>/",getLastestICDone),
   path("Indices/HistoricCap/",getHistoricCap),
   path("Indices/Impact/",getIndicesImpact),
   path("Indices/HH/",getIndicesHH),
   path("IndsutriesPage/",getAllIndustriesData),
   path("ImpactOnIndex",getImpactOnIndex),
   path("HHMarketDetails",getHHMarket),
   path("HighestDemands",getHighestDemands),
   path("HighestSupplies",getHighestSupplies),
   path("HighestQ",getHighestQ),
   path("Dashboard",getAllDashboard),
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
   path("Ticker/TechnicalIndicators/<identifier>/",getIndicators),
   path("Ticker/TechnicalIndicatorSingle/<identifier>/",getIndicators2),
   path("Ticker/TechnicalIndicatorsAll",getIndicatorsAll),
   path("IndexDetails/<identifier>/",getIndexDetails),
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
   path("Monthly/Service/<identifier>/",getMonthlyServices),
   path("Monthly/Leasing/Cost/<identifier>/",getMonthlyLeasingCost),
   path("Monthly/Leasing/Delegated/<identifier>/",getMonthlyLeasingDelegated),
   path("Monthly/Leasing/Revenue/<identifier>/",getMonthlyLeasingRevenue),
   path("Monthly/Investment/InTransactions/<identifier>/",getMonthlyInvestment_InTrans),
   path("Monthly/Investment/OutTransactions/<identifier>/",getMonthlyInvestment_OutTrans),
   path("Monthly/Investment/Portfolio/<identifier>/",getMonthlyInvestment_Portfo),
   path("Monthly/Investment/Summary/<identifier>/",getMonthlyInvestment_Summary),
   path("Statement/BalanceSheet/<identifier>/",getBalanceSheetAll),
   path("Statement/IncomeStatement/<identifier>/",getIncomeStatementAll),
   path("Statement/CashFlow/<identifier>/",getCFAll),
############

   path("CurrentBoard/<identifier>/",getCurrentBoard),
   path("CurrentCeo/<identifier>/",getCurrentCeo),
   path("AdminNotices/<firm>/",getAdminNotice),
   path("StatusChanges/<identifier>/",getStatusChanges),
   path("Shareholders/<identifier>/",getShareHolders),
   ####
   path("IndexMarketCap",getIndexMarketCap),
   path("ViewOptionAssetVolatility",getOptionAssets),
   path("TapeData",getTape),
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

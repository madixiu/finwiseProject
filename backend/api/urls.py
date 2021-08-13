
from django.urls import path,re_path
from .views import *


urlpatterns = [
   # re_path(r'^get-token/$', get_csrf_token),

   ## OPTION
   path("options", getOptions),
   path("ViewOptionAssetVolatility",getOptionAssets),

   path("tickerallnames",getTickersNames),
   path("tableallnames",getTableNames),
   path("findTickerid",findTickerID),
   
   ## MARKET WATCH
   path("marketwatch",getMarketWatch),
   path("marketwatchfilterlists",getMarketWatchFilters),

   ##? DASHBOARD ##
   path("ImpactOnIndex",getImpactOnIndex),
   path("getHighestValue",getHighestValue),
   path("getAllTradesValue",getAllTradesValue),
   path("LatestNews",getLatestNews),
   path("getTodayTepix",getTodayTepix),
   path("HHMarketDetails",getHHMarket),
   path("HighestDemands",getHighestDemands),
   path("HighestSupplies",getHighestSupplies),
   path("HighestQ",getHighestQ),


   path("TradeValue/HH/Total",getTVHHTotal),
   path("TradeValue/HH/Asset",getTVHHAsset),
   path("TradeValue/Asset",getTVAssets),
   path("LatestTepixIFB",getIFBTEPIX),
   path("LatestIC",getLastestIC),
   path("LatestICDone/<identifier>/",getLastestICDone),
   path("Indices/HistoricCap/",getHistoricCap),
   path("Indices/Impact",getIndicesImpact),
   path("Indices/HH",getIndicesHH),
   path("IndsutriesPage",getAllIndustriesData),

   path("Dashboard",getAllDashboard),
   ######
   ######
   path("CodalNotices",getCodalNoticesAll),
   path("CodalNotices/<identifier>/",getCodalNoticesAll),
   path("SubHeaderW/<identifier>/",getSubHeader),
   path("HHhistoryGraph/<identifier>/",getHHhistory),
   path("AdjustedPrices/<identifier>/",getAdjustedPriceHistory),
   path("AdjustedPricesCodal/<identifier>/",getAdjustedPriceHistoryCodal),
   path("StatsTicker/<identifier>/",getStatsTicker),
   path("LiveHHTicker/<identifier>/",getLiveHHTicker),
   path("LiveTicker/<identifier>/",getLiveTicker),
   path("Fundamental/ValuationRatio/<identifier>/",getValuationRatios),
   path("Ticker/TechnicalIndicators/<identifier>/",getIndicators),
   path("Ticker/TechnicalIndicatorSingle/<identifier>/",getIndicators2),
   path("Ticker/TechnicalIndicatorsAll",getIndicatorsAll),
   path("Ticker/TechnicalTrends/<identifier>/",getTechnicalTrends),
   path("IndexDetails/<identifier>",getIndexDetails),
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
   path("Monthly/ProductionAnalysis1/<identifier>/",getMonthlyProductionAnalysis1),
   
   path("Monthly/Service/<identifier>/",getMonthlyServices),
   path("Monthly/Leasing/Cost/<identifier>/",getMonthlyLeasingCost),
   path("Monthly/Leasing/Delegated/<identifier>/",getMonthlyLeasingDelegated),
   path("Monthly/Leasing/Revenue/<identifier>/",getMonthlyLeasingRevenue),
   path("Monthly/Investment/InTransactions/<identifier>/",getMonthlyInvestment_InTrans),
   path("Monthly/Investment/OutTransactions/<identifier>/",getMonthlyInvestment_OutTrans),
   path("Monthly/Investment/Portfolio/<identifier>/",getMonthlyInvestment_Portfo),
   path("Monthly/Investment/Summary/<identifier>/",getMonthlyInvestment_Summary),
   path("Statement/BalanceSheet/<identifier>/",getBalanceSheetAll),
   path("Statement/BalanceSheetAggregated/<identifier>/",getBalanceSheetAllAggregated),
   path("Statement/IncomeStatement/<identifier>/",getIncomeStatementAll),
   path("Statement/IncomeStatementAggregated/<identifier>/",getIncomeStatementAllAggregated),
   path("Statement/CashFlow/<identifier>/",getCFAll),
############
   ###Crypto
   path("CryptoTechincalAll/",getAllCryptoTechnical),
   path("CryptoHistoricCorr",getCryptoCorr),
   path("CryptoSingleBasic/<identifier>/",getBasicCrypto),
   path("CryptoSingleLive/<identifier>/",getCryptoLive),
   path("Crypto/TechnicalIndicatorSingle/<identifier>/",getIndicatorsCrypto),
   path("Crypto/Marketwatch/",getCyptoMWIntro),
   path("Crypto/MarketwatchAll/",getCyptoMWAll),
   ######
   path("CurrentBoard/<identifier>/",getCurrentBoard),
   path("CurrentCeo/<identifier>/",getCurrentCeo),
   path("AdminNotices/<firm>/",getAdminNotice),
   path("StatusChanges/<identifier>/",getStatusChanges),
   path("Shareholders/<identifier>/",getShareHolders),
   ####
   path("IndexMarketCap",getIndexMarketCap),
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


   ### TRADING VIEW
   path("TVData/<limits>/<url>/<todate>/<typeOf>",getTradingViewData),
   path("TVData/listOfStocks",getTradingViewList),

   ###
   path("HaghTaghadom",getHaghTaghadom),
   path("Oragh",getOragh),
   path("Funds",getFunds),
   path("FundsAll",getNewFunds),
   path("CryptoMarket",getCrypto),

   ##? Commodity
   path("Commodities/IR",getCommoditiesBasic),
   path("Commodities/Investing",getCommoditiesBasicInvesting),
   path("Commodities/Petro",getCommoditiesPetro),
   path("Commodities/MB",getCommoditiesMB),
   path("CommoditiesDetail/IR/<identifier>",getCommoditiesDetailIR),
   path("CommoditiesDetail/IN/<identifier>",getCommoditiesDetailInvesting),
   path("CommoditiesDetail/PL/<identifier>",getCommoditiesDetailPlats),
   
   ##? funds
   path("Funds/FundsMeta/<identifier>/",getFundsMeta),
   path("Funds/FundsIndustry/<identifier>/",getFundsIndustryComp),
   path("Funds/FundsAsset/<identifier>/",getFundsAssetComp),
   path("Funds/FundsHistoricNAV/<identifier>/",getFundsHistoricalNav),
   path("Funds/FundsLive/<identifier>/",getFundsLiveNAV),

]

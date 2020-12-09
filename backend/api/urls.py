
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
   ######
   path("tse/top5MostViewed/",getTop5MostViewed),
   ######
   path("CodalNotices",getCodalNoticesAll),
   path("CodalNotices/<identifier>/",getCodalNoticesAll),
   path("SubHeaderW/<identifier>/",getSubHeader),
   path("HHhistoryGraph/<identifier>/",getHHhistory),
   path("AdjustedPrices/<identifier>/",getAdjustedPriceHistory),
   path("StatsTicker/<identifier>/",getStatsTicker),
   path("Alldps/<identifier>/",getAllDPS),
   ####Monthly
   path("Monthly/Type/<identifier>/",getTypeOfMonthly),
   path("Monthly/Bank/Deposits/<identifier>/",getMonthlyBank_Deposits),
   path("Monthly/Bank/Facilities/<identifier>/",getMonthlyBank_Facility),
   path("Monthly/Insurance/<identifier>/",getMonthlyInsurance),
   path("Monthly/Construction/Ongoing/<identifier>/",getMonthlyConstOngoing),
   path("Monthly/Construction/Sold/<identifier>/",getMonthlyConstSold),
   path("CurrentBoard/<identifier>/",getCurrentBoard),
   path("CurrentCeo/<identifier>/",getCurrentCeo),
   path("AdminNotices/<firm>/",getAdminNotice),
   path("StatusChanges/<identifier>/",getStatusChanges),
   ####
   path("IndexMarketCap",getIndexMarketCap)
   
]

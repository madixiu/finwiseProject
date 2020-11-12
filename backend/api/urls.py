
from django.urls import path,re_path
from .views import getOptions, getTickersNames,findTickerID,getTableNames,getMarketWatch,getMarketWatchFilters


urlpatterns = [
   # re_path(r'^get-token/$', get_csrf_token),
   path("options", getOptions),
   path("tickerallnames",getTickersNames),
   path("tableallnames",getTableNames),
   path("findTickerid",findTickerID),
   path("marketwatch",getMarketWatch),
   path("marketwatchfilterlists",getMarketWatchFilters)

]

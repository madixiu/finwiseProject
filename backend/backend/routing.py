from websocket.consumers import *
from django.urls import re_path,path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
# from channels.sessions import SessionMiddlewareStack

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    # re_path(r"^messages/(?P<username>[\w.@+-]+)/$", firm_live), # noqa
                    re_path(r"^ws/taghadom",getTaqadom .as_asgi()), ## HaghTaghadom
                    re_path(r"^ws/oraq",getOraq .as_asgi()), ##Oraq
                    re_path(r"^ws/funds",getFunds .as_asgi()), ##Sandoq
                    re_path(r"^ws/options",getOptions .as_asgi()), ## Option
                    re_path(r"^ws/marketmap",getMarketMap .as_asgi()), ## MarketMap
                    re_path(r"^ws/marketwatch",getMarketWatch .as_asgi()), ## MarketWatch
                    re_path(r"^ws/liveTickerData",getLiveTicker .as_asgi()),
                    re_path(r"^ws/Top5Views",Top5Viewed .as_asgi()),
                    re_path(r"^ws/ImpactOnIndex",getImpactOnIndex .as_asgi()),
                    re_path(r"^ws/HighestVolume",getHighestVolumes .as_asgi()),
                    re_path(r"^ws/HighestValues",getHighestValues .as_asgi()),
                    re_path(r"^ws/HighestSupplies",getHighestSupplies .as_asgi()),
                    re_path(r"^ws/HighestDemands",getHighestDemand .as_asgi()),
                    re_path(r"^ws/Crypto",getCrypto .as_asgi()),                    
                    re_path(r"^ws/IRCommodities",getIRCommodities .as_asgi()),                    
                    re_path(r"^ws/InvCommodities",getInvestingCommodities .as_asgi()),    

                ]
            )
        )
    )
})

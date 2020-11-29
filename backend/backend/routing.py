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
                    re_path(r"^ws/test$", optionData),
                    # re_path(r"^index_live/$", index_live),
                    re_path(r"^random$", random),
                    re_path(r"^marketwatch",MarketWatch),
                    re_path(r"^Top5Views",Top5Viewed .as_asgi()),
                    re_path(r"^ImpactOnIndex",getImpactOnIndex .as_asgi()),
                    re_path(r"^HighestVolume",getHighestVolumes .as_asgi()),
                    re_path(r"^HighestValues",getHighestValues .as_asgi()),
                    re_path(r"^HighestSupplies",getHighestSupplies .as_asgi()),
                    re_path(r"^HighestDemands",getHighestDemand .as_asgi()),

                ]
            )
        )
    )
})

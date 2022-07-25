"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Fetch Django ASGI application early to ensure AppRegistry is populated
# before importing consumers and AuthMiddlewareStack that may import ORM
# models.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django_asgi_app = get_asgi_application()

# import django
# from channels.routing import get_default_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from websocket.consumers import random
from django.urls import re_path



# django.setup()
# application = get_default_application()
application = ProtocolTypeRouter({
     # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter(
             [
                    # re_path(r"^messages/(?P<username>[\w.@+-]+)/$", firm_live), # noqa
                    re_path(r"^ws/wstest",random .as_asgi()), ## HaghTaghadom
                    # re_path(r"^ws/oraq",getOraq .as_asgi()), ##Oraq
                    # re_path(r"^ws/funds",getFunds .as_asgi()), ##Sandoq
                    # re_path(r"^ws/options",getOptions .as_asgi()), ## Option
                    # re_path(r"^ws/marketmap",getMarketMap .as_asgi()), ## MarketMap
                    # re_path(r"^ws/marketwatch",getMarketWatch .as_asgi()), ## MarketWatch
                    # re_path(r"^ws/liveTickerData",getLiveTicker .as_asgi()),
                    # re_path(r"^ws/Top5Views",Top5Viewed .as_asgi()),
                    # re_path(r"^ws/ImpactOnIndex",getImpactOnIndex .as_asgi()),
                    # re_path(r"^ws/HighestVolume",getHighestVolumes .as_asgi()),
                    # re_path(r"^ws/HighestValues",getHighestValues .as_asgi()),
                    # re_path(r"^ws/HighestSupplies",getHighestSupplies .as_asgi()),
                    # re_path(r"^ws/HighestDemands",getHighestDemand .as_asgi()),
           

                ]
        )
    ),
})

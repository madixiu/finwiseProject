from websocket.consumers import optionData
from django.urls import re_path
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
                    # re_path(r"^random/$", random)


                ]
            )
        )
    )
})

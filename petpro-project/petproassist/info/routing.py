from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from . import consumers
from info.consumers import YourConsumer, MyConsumer 

websocket_urlpatterns = [
    path("ws/some_path/", consumers.VotreConsumer.as_asgi()),
    re_path(r"ws/some_path/(?P<param>\w+)/$", YourConsumer.as_asgi()),
    re_path(r'ws/some_path/$', MyConsumer.as_asgi()),
    # Ajoutez d'autres routes WebSocket au besoin
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})

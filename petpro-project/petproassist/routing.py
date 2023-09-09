from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
import info.routing  

application = ProtocolTypeRouter({
    # Autres protocoles (HTTP, Websockets, etc.)
    'websocket': URLRouter([
        path('ws/some_path/', VotreConsumer.as_asgi()),  # Spécifiez l'URL de la messagerie WebSocket et le consumer approprié
    
    ]),
})
application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(info.routing.websocket_urlpatterns)
        ),
    }
)
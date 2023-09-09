from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from django.contrib.sessions.models import Session

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Logique de connexion
        user = self.scope["user"]
        session_key = self.scope.get("session").session_key

        if user.is_authenticated:
            # L'utilisateur est authentifié, autorisez la connexion WebSocket
            await self.accept()

            if session_key:
            # Récupérez la session Django associée à l'ID de session
                session = await self.get_session(session_key)

                if session and session.get("websocket_token"):
                # Vérifiez le token WebSocket et autorisez la connexion si valide
                    await self.accept()
                    #return
        else:
            # L'utilisateur n'est pas authentifié, refusez la connexion WebSocket
            await self.close()
        #pass

    async def disconnect(self, close_code):
        # Logique de déconnexion
        #pass
        await self.channel_layer.group_discard("nom_du_groupe", self.channel_name)

    async def receive(self, text_data):
        # Logique de réception de messages
        #pass
        await self.send(text_data=json.dumps({"message": "Message reçu"}))

    @database_sync_to_async
    def get_session(self, session_key):
        try:
            return Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            return None

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Traitez le message reçu (text_data) ici
        message = json.loads(text_data)
        content = message['content']

        # Répondez au client si nécessaire
        await self.send(text_data=json.dumps({
            'type': 'chat.message',
            'content': content,
        }))
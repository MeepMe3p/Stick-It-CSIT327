from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import User,AnonymousUser

import json

# @database_sync_to_async
# def creaate_notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self,event):
        print("connected", event)
        print("hello deerr")
        print(self.scope['url_route']['kwargs']['pk'])
        self.user = f"user_{self.scope['url_route']['kwargs']['pk']}"
        # print(self.scope)
        
        # self
        await self.channel_layer.group_add(self.user, self.channel_name)
        await self.accept()
        # await self.send(json.dumps({
        #     "type":"websocket.send",
        #      "text":"hello word",
        # }))


    async def websocket_disconnect(self, code):
        await(self.channel_layer.group_discard(self.scope['user'].id),self.channel_name)

    # def receive(self, text_data=None, bytes_data=None):
    #     text_data = json.loads(text_data)
    #     notif = text_data_json['message']
    #     self.send(text_data=json.dumps({"message":notif}))

@database_sync_to_async
def get_user(pk):
    try:
        return User.objects.get(pk=pk)
    except:
        return AnonymousUser()
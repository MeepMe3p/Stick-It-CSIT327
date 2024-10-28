from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import User,AnonymousUser
from .models import Notifications,Board

import json

# @database_sync_to_async
# def creaate_notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print("connected", event)
        print("hello deerr")
        self.user = f"user_{self.scope['url_route']['kwargs']['pk']}"
        print(self.user)
        
        # self.user = f"user_{self.scope['url_route']['kwargs']['pk']}"
  
        print("niconnet sha so goods na")
        await self.channel_layer.group_add(self.user, self.channel_name)
        await self.accept()



    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(self.user,self.channel_name)

    async def receive(self,text_data):
        print("receiveeeed na baaaa!!!! di ka mareceive dasok tika diri")
        text_data_json = json.loads(text_data)
        message = text_data_json
        print(message)
        await self.channel_layer.group_send(
            self.user,{
                "type": "send_message",
                "message": message
            }
        )

    async def send_message(self,event):
        data = event['message']
        print("nipasok ka diri")
        await self.create_notification(data=data)
        response_data = data
        await self.send(text_data=json.dumps({'message':response_data}))

    @database_sync_to_async
    def create_notification(self,data):
        # diri ang magic
        user_sender = User.objects.get(id=data['sender'])
        users_added = data['added']
        users_removed = data['removed']
        
        if users_added:
            for users in users_added:
                print(users)
                user_receiver = User.objects.get(id=users)

                notif = Notifications(user_sender = user_sender, user_receiver = user_receiver, notif_detail = data['message_add'], notif_time = data['time_sent'])
        if users_removed:
            for users in users_removed:
                print(users)
                user_receiver = User.objects.get(id=users)

                notif = Notifications(user_sender = user_sender, user_receiver = user_receiver, notif_detail = data['message_removed'], notif_time = data['time_sent'])

        board = Board.objects.get(pk =data['board'])
        # board.users.remove(users_removed)
        print(users_added)


import json
from django.core.serializers import serialize
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from note.models import *
class NoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.note_board_name = f"board_{self.scope['url_route']['kwargs']['note_board_name']}"

        await self.channel_layer.group_add(self.note_board_name, self.channel_name)
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.note_board_name, self.channel_name)
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        note = data['note']
        state = data['state']
        # Save note to database
        if state == 'create':
            note = await self.save_note_to_db(note)
            # Broadcast the note to other clients
            await self.channel_layer.group_send(
                self.note_board_name,
                {
                    'type': 'send_note',
                    'note': note,
                    'state' : 'create'
                }
            )
        if state == 'move':
            await self.channel_layer.group_send(
                self.note_board_name,
                {
                    'type': 'send_note',
                    'note': note,
                    'state' : 'move'
                }
            )
        if state == 'delete':
            # Broadcast the note to other clients
            await self.channel_layer.group_send(
                self.note_board_name,
                {
                    'type': 'send_note',
                    'note': note,
                    'state' : 'delete'
                }
            )
        if state == 'input':
            # Broadcast the note to other clients
            await self.channel_layer.group_send(
                self.note_board_name,
                {
                    'type': 'send_note',
                    'note': note,
                    'state' : 'input'
                }
            )
    # This method handles the broadcast and sends it to all connected WebSocket clients
    async def send_note(self, event):
        # Prepare the data that will be sent back to the clients
        event_state = event['state']
        if event_state == "create":
            note_data = serialize('json', [event['note']])
        else:
            note_data = event['note']
            
        response_data = {
            'note': note_data,
            'state' : event_state
        }
        print("Response: ", response_data)
        await self.send(text_data=json.dumps(response_data))
        
    @database_sync_to_async
    def save_note_to_db(self, data):
        content = data.get('content')
        borderColor = data.get('borderColor')
        coordinates = data.get('coordinates')
        is_finished = data.get('is_finished')
        checkbox_id = data.get('checkbox_id')
        
        # Save note to database
        note = Note.objects.create(
            content=content,
            border_color=borderColor,
            coordinates=coordinates,
            is_finished=is_finished,
            checkbox_id=checkbox_id
        )
        return note
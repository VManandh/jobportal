# from channels.generic.websocket import AsyncWebsocketConsumer

# class EchoConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         # When browser connects
#         await self.accept()

#     async def receive(self, text_data):
#         # When browser sends message
#         await self.send(text_data=text_data)

#     async def disconnect(self, close_code):
#         # When browser disconnects
#         pass
# ----------------------------------------------------------------------------


import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = "global_chat"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=event["message"])

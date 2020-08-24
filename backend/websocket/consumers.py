import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.exceptions import StopConsumer
# from channels.db import database_sync_to_async
# from .models import Thread, ChatMessage
# from .ApiGet import publicApi, realTimePublicApi
# from .randomGen import get_number
from .getOptions import optionRequest, optionFlag

class optionData(AsyncWebsocketConsumer):
    channel_layer = get_channel_layer()
    # groups = ["options"] 


    async def connect(self):
        channel_layer = get_channel_layer()
        print(str(channel_layer))
        # print(str(self.scope["session"]["seed"]))
        print('WEBSOCKET BACKEND CONNECTED!')
        await self.accept()
        while(True):
            if(optionFlag()):
                await self.send(text_data = optionRequest())
                print('fuck')
            await asyncio.sleep(10)
#             await self.send({
#                 "type": "websocket.send",
#                 "text": str(get_number())

#             })
#             await asyncio.sleep(1)

        

            # await self.send({
            #     "type": "websocket.send",
            #     "text": json.dumps(optionRequest())
            # })
            # await asyncio.sleep(15)
        #######################################

        # await self.send({
        #     "type": "websocket.send",
        #     "text": "hello world"
        # })
    # async def websocket_receive(self, event):
    #     # when a message is received from the websocket
    #     print("receive", event)
    #     front_text = event.get('text', None)
    #     if front_text is not None:
    #         loaded_dict_data = json.loads(front_text)
    #         msg = loaded_dict_data.get('message')
    #         print(msg)

    async def websocket_disconnect(self, event):
        print("optionData", event)
        await self.channel_layer.group_discard(
        self.room_name,
        self.channel_name)
        raise StopConsumer()

    # @database_sync_to_async
    # def get_thread(self,user,other_username):
    #     return Thread.objects.get_or_new(user,other_username)[0]


# class index_live(AsyncConsumer):
#     async def websocket_connect(self, event):
#         # print("connected", event)
#         # print(realTimePublicApi())
#         await self.send({
#             "type": "websocket.accept"
#         })
#         await self.send({
#             "type": "websocket.send",
#             "text": realTimePublicApi()
            

#         })

#         # print(realTimePublicApi())
# class random(AsyncConsumer):
#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept"
#         })
#         while(True):
#             await self.send({
#                 "type": "websocket.send",
#                 "text": str(get_number())

#             })
#             await asyncio.sleep(1)

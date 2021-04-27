import asyncio
import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.exceptions import StopConsumer
# from channels.db import database_sync_to_async
# from .models import Thread, ChatMessage
# from .ApiGet import publicApi, realTimePublicApi
from .randomGen import get_number
from requestcall.getOptions import optionRequest
from requestcall.getMarketWatch2 import getMarketWatchRequest,getFilteredData
from requestcall.treeMapData import getMapData
from requestcall.getTseData import *
from requestcall.getOragh_HaghTaghadom_FundsData import *


## option section
# class optionData(AsyncWebsocketConsumer):
#     channel_layer = get_channel_layer()


#     async def connect(self):
#         channel_layer = get_channel_layer()
#         print(str(channel_layer))
#         print('WEBSOCKET BACKEND CONNECTED!')
#         await self.accept()
#         while(True):
#             # if(optionFlag()):
#             await self.send(text_data = optionRequest())
            
#             await asyncio.sleep(10)

#     async def websocket_disconnect(self, event):
#         print("optionData", event)
#         await self.channel_layer.group_discard(
#         self.room_name,
#         self.channel_name)
#         raise StopConsumer()

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
class random(AsyncWebsocketConsumer):
    channel_layer = get_channel_layer()
    is_connected = False
    print("channel layer:" + str(channel_layer))
    async def connect(self):
        await self.accept()
        
        self.is_connected = True
        # while (self.is_connected):
        #     await self.send(text_data=str(get_number()))
        #     await asyncio.sleep(5)
            
      
        # await self.close()

        # await self.send({
        #     "type": "websocket.accept"
        # })
        
        # await self.send({
        #     "type": "websocket.send",
        #     "text": str(get_number())

        # })
    async def receive(self,text_data):
        data = json.loads(text_data)
      
        if data[0].get("request") == "live":
            await self.send(text_data = str(get_number()))
        elif data[0].get("request") == "get":
            print(data[1])

        elif data[0].get("request") == "halt":
            await self.close()

    async def disconnect(self, close_code):
        print("randomWS", close_code)
        # await self.channel_layer.group_discard(
        # self.room_name,
        # self.channel_name)
        self.is_connected = False
        self.close()
        raise StopConsumer()


class MarketWatch(AsyncWebsocketConsumer):
    channel_layer = get_channel_layer()
    async def connect(self):
        await self.accept()
        print("connected to Ws MarketWatch")
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data[0].get("request") == "get":
            # print('req')
            # print(data)
            # dic = {}
            # dic['data'] = getMarketWatchHeaderReq()
            text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            # text_data = json.dumps(getMarketWatchRequest())
            await self.send(text_data)
            # await asyncio.sleep(2)
            return
        if data[0].get("request") == "halt":
            return
            

    async def disconnect(self, code):
        # print("MarketWatchWS", code)
        self.close()
        raise StopConsumer()

class Top5Viewed(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(Top5MostViewed());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()    
class getImpactOnIndex(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(ImpactOnIndex());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()        
class getHighestVolumes(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(highestTvolumes());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()        
class getHighestValues(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(highestTvalues());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()        
class getHighestDemand(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(highestDemands());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()        
class getHighestSupplies(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            # print('req')
            text_data = json.dumps(highestSupplies());
            # text_data = json.dumps(getFilteredData(data[1].get("marketName"),data[1].get("marketType"),data[1].get("marketIndustry")))
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()

class getMarketWatch(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(getFilteredData(data.get("data").get("marketName"),data.get("data").get('marketIndustry')));
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()
        # return super().disconnect(code)

class getMarketMap(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(getMapData());
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 

class getOptions(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(optionRequest());
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 

class getLiveTicker(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps([getLive_ticker(data.get("id")),getLiveHHtickerData(data.get("id"))]);
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 

#############################################################
class getFunds(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(getFundsData());
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 

#############################################################
class getOraq(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(getOraghData());
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 

#############################################################
class getTaqadom(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("request") == "get":
            text_data = json.dumps(getHaghTaghadomData());
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer() 
##############################################################
class getCrypto(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        if data.get("request") == "get":
            text_data = json.dumps(getCryptoMarketData());
            
            await self.send(text_data)
            return
        if data.get("request") == "halt":
            return
    async def disconnect(self, code):
        self.close()
        raise StopConsumer()         
from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from . models import *
from channels.db import  database_sync_to_async
class MySyncConsumers(SyncConsumer):

    def websocket_connect(self,event):
        async_to_sync(self.channel_layer.group_add)("Trains" , self.channel_name)
        self.send({
            'type':'websocket.accept'
        })


    def websocket_receive(self,event):
        data = json.loads(event['text'])
        new_data=TrainDetails.objects.get(id=int(data['msg'].split(" ")[0]))
        new_data.status=data['msg'].split(" ")[1]
        new_data.save()
        content= TrainDetails.objects.values('id','name','status')
        s=json.dumps(list(content))

        async_to_sync(self.channel_layer.group_send)('Trains',{
            'type':'chat.message',
            'message':s
        })

    def chat_message(self,event):

        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self,event):
        print("connection closed " , event)
        self.channel_layer.group_discard('programmers', self.channel_name)
        raise StopConsumer()



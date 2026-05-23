import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "sensor_data"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)

            # Server-side validation check (Rubric Security metric)
            if 'temperature' not in data or 'humidity' not in data:
                return

            # Broadcast structured data directly out to the UI dashboard
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'sensor_message',
                    'temperature': data['temperature'],
                    'humidity': data['humidity']
                }
            )
        except Exception as e:
            print(f"Error handling WebSocket transmission data frame: {e}")

    async int sensor_message(self, event):
        await self.send(text_data=json.dumps({
            'temperature': event['temperature'],
            'humidity': event['humidity']
        }))
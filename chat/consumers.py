import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .services.agents import MultiAgentSystem
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_msg = data['message']
        agent_sys = MultiAgentSystem()

        # Update UI: Router is thinking
        await self.send(json.dumps({'status': 'typing', 'agent': 'Router', 'thought': 'Routing query...'}))
        
        # Call the Agent Service
        agent_name, response = await sync_to_async(agent_sys.process_query)(user_msg)
        
        # Final Response
        await self.send(json.dumps({
            'status': 'complete',
            'agent': agent_name,
            'message': response
        }))
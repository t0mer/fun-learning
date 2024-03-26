from fastapi import WebSocket

class ConnectionManager:
    """Class defining socket events"""
    def __init__(self) -> None:
        self.connections  = {}
 
    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.connections[user_id] = websocket

    async def disconnect(self, user_id):
        websocket: WebSocket = self.connections[user_id]
        await websocket.close()
        del self.connections[user_id]

    async def send_messages(self, user_ids, message):
        for user_id in user_ids:
            websocket: WebSocket = self.connections[user_id]
            await websocket.send_text(message)

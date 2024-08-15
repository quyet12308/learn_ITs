from fastapi import WebSocket
from typing import List, Dict


class ChatRoom:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    async def disconnect(self, websocket: WebSocket, room_id: str):
        self.active_connections[room_id].remove(websocket)
        if not self.active_connections[room_id]:
            del self.active_connections[room_id]

    async def send_message(self, websocket: WebSocket, room_id: str, message: str):
        for connection in self.active_connections.get(room_id, []):
            if connection != websocket:
                await connection.send_text(message)


chat_room = ChatRoom()

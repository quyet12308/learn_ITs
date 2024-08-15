from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from chat import chat_room
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Điều chỉnh cho phù hợp với môi trường thực tế của bạn
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    return {"message": "Welcome to the Realtime Chat Room"}


@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await chat_room.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            await chat_room.send_message(websocket, room_id, data)
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        await chat_room.disconnect(websocket, room_id)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=9000)

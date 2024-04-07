

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print(f"Sent name to server : {name}")

        greeting = await websocket.recv()
        print(f"Recieved greeting from server {greeting}")
        await messages(websocket)

async def messages(websocket):
    while True:
        message = input("Enter message to send to server : ")
        await websocket.send(message)
        if(message == 'exit'):
            break
        


if __name__ == "__main__":
    asyncio.run(hello())
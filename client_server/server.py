import asyncio
import websockets

clients = []

def addClient(name):
    clients.append(name)
    

async def hello(websocket):
    name = await websocket.recv()
    print(f"Recieved name from client : {name}")

    greeting = f"Hello {name}!"
    addClient(name)
    print(f'Connected clients \n {clients}')        

    await websocket.send(greeting)
    print(f"Sent greeting to client : {greeting}")
    await messages(websocket,name)
    print(f'clients available {clients}')


async def messages(websocket,name):
    while(True):
        message = await websocket.recv()
        print(f'Client sent : {message}')
        if(message == 'exit'):
            clients.remove(name)
            break
    



async def main():
    async with websockets.serve(hello,"localhost",8765):
        print("The server is up!")
        await asyncio.Future() # Run forever
  

asyncio.run(main())

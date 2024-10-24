import asyncio
import websockets

# WebSocket client to connect to the server
async def vpn_client(uri):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        
        # Send a message to initiate connection
        await websocket.send("Client connected!")
        print(f"Sent: Client connected!")

        # Receive and print the server response
        response = await websocket.recv()
        print(f"Received: {response}")

        # Here, you can send/receive actual VPN data, configure routing, etc.
        while True:
            data = input("Enter data to send: ")
            await websocket.send(data)
            response = await websocket.recv()
            print(f"Received: {response}")

# Main loop to run the WebSocket client
if __name__ == "__main__":
    # Replace with the actual WebSocket server URI
    server_uri = "ws://localhost:8765"
    
    # Start the VPN client
    asyncio.get_event_loop().run_until_complete(vpn_client(server_uri))
    
 import asyncio
import websockets

# WebSocket server to handle client connections
async def vpn_handler(websocket, path):
    print("Client connected")
    
    # Handle receiving data from the client
    async for message in websocket:
        print(f"Received: {message}")
        
        # Echo the message back to the client
        await websocket.send(f"Server received: {message}")

# Start the WebSocket server
if __name__ == "__main__":
    start_server = websockets.serve(vpn_handler, "localhost", 8765)
    
    # Run the server until manually stopped
    asyncio.get_event_loop().run_until_complete(start_server)
    print("Server started at ws://localhost:8765")
    asyncio.get_event_loop().run_forever()
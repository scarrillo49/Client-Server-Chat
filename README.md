# Client-Server Chat Program

This chat application allows multiple users to join a chatroom and broadcast messages with random nicknames. It consists of two Python scripts: `server.py` and `client.py`.

## Instructions to Run the Code

1. **Set Host and Port**: Adjust the `host` and `port` variables in both `server.py` and `client.py` if necessary.

2. **Run the Server**:
   - Open a terminal and start the server with:
     ```bash
     python3 server.py
     ```
   - You should see "Server is listening" if it’s running successfully.

3. **Run the Client**:
   - In a new terminal, run the client with:
     ```bash
     python3 client.py
     ```
   - To simulate multiple users, run additional instances of `client.py` in separate terminals.
   - Each client will connect to the server, allowing users to type messages that will be broadcasted to all connected clients.

4. **Exit the Chat**:
   - To leave the chat, type `.exit` in the client terminal.
   - The client will disconnect, and the script will end.

## Server-Side Functions
The server manages client connections, broadcasts messages, and handles disconnections with the following functions:
- `generate_random_nickname()`: Assigns a unique nickname (e.g., "Client-123") to each user.
- `broadcast(message)`: Sends messages to all connected clients and removes any with errors.
- `receive()`: Accepts incoming connections, assigns nicknames, and sends a welcome message.
- `handle(client, nickname)`: Manages communication with each client; exits on ".exit".
- `handle_exit(client, nickname)`: Processes user exits, removes them, and notifies others.
- `handle_client_disconnection(client)`: Manages unexpected disconnections and alerts remaining clients.

## Client-Side Functions
The client connects to the server, enabling users to send and receive messages in real time through two threads:
- `generate_random_nickname()`: Generates a nickname for the user.
- `receive()`: Continuously listens for messages from the server; closes connection on ".exit".
- `send()`: Prompts the user for input, sends messages, and exits on ".exit".

The client’s send and receive functions run concurrently, allowing seamless chat functionality.

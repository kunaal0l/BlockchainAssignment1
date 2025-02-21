# Peer-to-Peer Chat Application

## Team Details

**Team Name**: XYZ

**Team Members**:
- Kunal Gourv (230002036)
- Kumar Ayaman (230001044)
- Cheepati Gireesh Kumar Reddy (230005013)

---

## Overview
This repository contains a Python implementation of a peer-to-peer chat application using TCP sockets and multithreading. The application enables users to send and receive messages simultaneously, maintain an active peer list, and establish connections dynamically.  

The program ensures reliable communication by utilizing a message format that includes the sender’s IP, port, team name, and the actual message. Fixed port numbers are assumed for all users, entered at startup to avoid duplicate entries for the same peer.

Our code also **handles the bonus requirement** by allowing users to initiate connections with active peers that have not yet been contacted.

---

## Implementation Details

### 1. Maintaining Active Peers List
The application maintains a dynamic set of active peers (peers that are available and eligible for connection). Each peer is stored as an (IP, PORT) tuple. The peer list is updated based on received messages:  
- If a message is received from a new peer, it is added to the list automatically.  
- If a peer sends a **"connect"** message, they are explicitly marked as connected.  
- If a peer sends an **"exit"** message, they are removed from the list.  
- If the user quits, the **"exit"** message is sent to all peers before termination.

### 2. Connection Management
Each peer's connection status is dynamically tracked. Users can manually initiate a connection by selecting from the active peers list. A connection message **"connect"** is sent to notify the selected peer.

### 3. Server & Listener Thread
A dedicated server thread listens for incoming messages and updates the active peer list accordingly. The server runs on the specified port, allowing real-time message handling and event-based notifications:
- New peer detection and addition.
- Connection confirmation when a **"connect"** message is received.
- Notification of incoming messages.
- Automatic peer removal on **"exit"** messages.

---

## Customizations

### 1. Initial Peer Discovery
The program includes a predefined list of **mandatory peers** to whom a **"hello"** message is sent at startup. This can be modified in the `mandatory_peers` list in the script.

### 2. Message Format
All messages follow the format:
```txt
<sender_ip>:<sender_port> <team_name> <message>
```
This format ensures that messages can be tracked and processed correctly by all peers.

---

## How to Run?
1. Ensure you have **Python 3.x** installed on your system.
2. Run the script using:
   ```sh
   python script.py
   ```
3. Enter your **name** and **port number** when prompted.
4. The server starts listening for incoming connections automatically.
5. Use the menu to:
   - **Send messages** to a specific peer by entering their IP and port.
   - **Query active peers** currently known to the system.
   - **Connect to a peer** to establish a formal connection.
   - **Exit**, which sends an **"exit"** message to all peers before quitting.

---

## Example Usage
```sh
Enter your name: Alice
Enter your port number: 5000
Server listening on 192.168.1.10:5000

***** Menu *****
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
Enter choice: 1
Enter the recipient's IP address: 192.168.1.12
Enter the recipient's port number: 6000
Enter your message: Hello there!
Sent to 192.168.1.12:6000: 192.168.1.10:5000 Alice Hello there!
```

---

## Acknowledgements
- **Prof. Subhra Mazumdar**, for guidance on peer-to-peer networking concepts.
- **GeeksforGeeks** for comprehensive documentation on [Python Socket Programming](https://www.geeksforgeeks.org/socket-programming-python/).

# Peer-to-Peer Chat Application

## Team Details

**Team Name**: Xyz

**Team Members**:
- Kunal Gourv (230002036)
- Kumar Ayaman (230001044)
- Cheepati Gireesh Kumar Reddy (230005013)

---

## Overview
This repository contains a Python-based peer-to-peer chat application using **TCP sockets** and **multithreading**. The application enables users to:
- Send and receive messages simultaneously.
- Maintain a dynamic list of active peers.
- Establish direct connections with other peers.
- Gracefully handle peer disconnections.

The system assumes fixed port numbers for each user, entered at startup. This prevents duplicate entries for the same peer and ensures smooth communication. Messages follow a standardized format, including sender IP, port, team name, and content.

Our implementation **includes the bonus feature**, allowing users to establish connections with active peers that have not yet been contacted.

---

## Implementation Details

### 1. Active Peer Management
The application maintains a **dictionary of active peers**, where each entry is stored as an `(IP, PORT) -> Team Name` mapping. The peer list is updated dynamically:
- If a message is **received from a new peer**, it is added to the list.
- If a **'connect'** message is received, the sender is marked as connected.
- If a **'exit'** message is received, the sender is removed from the list.
- If the user **quits**, an **'exit'** message is sent to all peers before termination.

### 2. Message Handling
Each message follows a **standard format**:
```txt
<sender_ip>:<sender_port> <team_name> <message>
```
This ensures that all peers can properly interpret incoming messages and track sender information.

A dedicated **server thread** listens for incoming messages and automatically updates the active peers list. It also handles peer disconnections and message notifications.

### 3. Connecting to Peers
The user can manually initiate a connection to any peer in the active peer list by selecting from the menu. A **'connect'** message is sent to formally establish a connection.

### 4. Predefined Peer Discovery
At startup, the application sends a **'hello'** message to a predefined list of peers (`mandatory_peers`). This ensures that users can establish an initial set of connections automatically.

---

## How to Run

1. Ensure **Python 3.x** is installed on your system.
2. Run the script using:
   ```sh
   python script.py
   ```
3. Enter your **name** and **port number** when prompted.
4. The server starts listening for incoming connections automatically.
5. Use the menu options to interact with peers:
   - **Send a message** to any peer.
   - **View active peers** currently known to the system.
   - **Connect to a peer** by selecting from the list.
   - **Exit**, which sends an **'exit'** message to all peers before quitting.

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

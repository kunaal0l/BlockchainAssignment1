import socket
import threading
import time


team_name = input("Enter your name: ").strip()
listening_port = int(input("Enter your port number: "))
own_ip = socket.gethostbyname(socket.gethostname())  
peer_list = {}  
lock = threading.Lock()  

def server():
    """Server thread to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', listening_port))  
    server_socket.listen(5)
    print(f"Server listening on {own_ip}:{listening_port}")
    while True:
        client_socket, addr = server_socket.accept()
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            
            parts = message.split(maxsplit=2)
            if len(parts) == 3:
                ip_port, team, msg = parts
                ip, port = ip_port.split(':')
                port = int(port)
                team = team.strip()
                with lock:
                    if msg.strip().lower() == "exit":
                        if (ip, port) in peer_list:
                            del peer_list[(ip, port)]
                            print(f"Peer {ip}:{port} ({team}) disconnected")
                    else:
                        peer_list[(ip, port)] = team
                        if msg.strip().lower() == "connect":
                            print(f"Connected to peer {ip}:{port} ({team})")
                        else:
                            print(f"{ip}:{port} {team} {msg}")
        client_socket.close()

def send_message(recipient_ip, recipient_port, message):
    """Send a message to a specified peer."""
    formatted_message = f"{own_ip}:{listening_port} {team_name} {message}"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((recipient_ip, recipient_port))
        client_socket.send(formatted_message.encode('utf-8'))
        print(f"Sent to {recipient_ip}:{recipient_port}: {formatted_message}")
        if (recipient_ip, recipient_port) not in peer_list:
            peer_list[(recipient_ip, recipient_port)] = "Unknown"
    except Exception as e:
        print(f"Failed to send message to {recipient_ip}:{recipient_port}: {e}")
    finally:
        client_socket.close()

def connect_to_peer():
    """Prompt the user to select a peer from the active peer list and send a 'connect' message."""
    with lock:
        if not peer_list:
            print("No active peers to connect to.")
            return
        print("Active Peers:")
        for idx, ((ip, port), name) in enumerate(peer_list.items(), start=1):
            print(f"{idx}. {ip}:{port} ({name})")
        try:
            choice = int(input("Enter the number of the peer to connect to: "))
            if 1 <= choice <= len(peer_list):
                selected_peer = list(peer_list.keys())[choice - 1]
                recipient_ip, recipient_port = selected_peer
                send_message(recipient_ip, recipient_port, "connect")
                print(f"Sent 'connect' to {recipient_ip}:{recipient_port}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

server_thread = threading.Thread(target=server, daemon=True)
server_thread.start()
time.sleep(0.1)
mandatory_peers = [
    ("10.206.4.122", 1255),
    ("10.206.5.228", 6555)
]
for ip, port in mandatory_peers:
    send_message(ip, port, "hello")

while True:
    print("\n***** Menu *****")
    print("1. Send message")
    print("2. Query active peers")
    print("3. Connect to active peers")
    print("0. Quit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        recipient_ip = input("Enter the recipient's IP address: ")
        recipient_port = int(input("Enter the recipient's port number: "))
        message = input("Enter your message: ")
        send_message(recipient_ip, recipient_port, message)
    elif choice == "2":
        with lock:
            if peer_list:
                print("Connected Peers:")
                for (ip, port), name in peer_list.items():
                    print(f"{ip}:{port} ({name})")
            else:
                print("No connected Peers")
    elif choice == "3":
        connect_to_peer()
    elif choice == "0":        
        with lock:
            for (ip, port) in list(peer_list.keys()):
                send_message(ip, port, "exit")
        print("Exiting")
        break
    else:
        print("Invalid choice")

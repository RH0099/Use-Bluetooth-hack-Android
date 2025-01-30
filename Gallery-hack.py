import bluetooth
import os
import sys

# Function to send a request to access the gallery
def send_request(target_address):
    try:
        # Create a Bluetooth socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, 1))  # Connect to the target device
        print("Connected to the target device.")

        # Send a request to access the gallery
        request_message = "REQUEST_GALLERY_ACCESS"
        sock.send(request_message)
        print("Request sent to the target device.")

        # Wait for the response
        response = sock.recv(1024).decode()
        if response == "ACCESS_GRANTED":
            print("Access granted. Fetching gallery...")
            # Simulate fetching gallery (for educational purposes only)
            print("Simulating gallery access...")
        else:
            print("Access denied by the target device.")

        sock.close()
    except Exception as e:
        print(f"Error: {e}")

# Function to handle incoming requests
def handle_request():
    try:
        # Create a Bluetooth socket
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]
        print(f"Waiting for connection on RFCOMM channel {port}...")

        # Accept a connection
        client_sock, client_info = server_sock.accept()
        print(f"Accepted connection from {client_info}")

        # Receive the request
        request = client_sock.recv(1024).decode()
        if request == "REQUEST_GALLERY_ACCESS":
            print("Request received: Access to gallery.")
            # Simulate a popup asking for permission
            permission = input("Do you want to allow access to your gallery? (yes/no): ").strip().lower()
            if permission == "yes":
                client_sock.send("ACCESS_GRANTED")
                print("Access granted.")
            else:
                client_sock.send("ACCESS_DENIED")
                print("Access denied.")

        client_sock.close()
        server_sock.close()
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    print("1. Send request to access gallery")
    print("2. Wait for incoming requests")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        target_address = input("Enter the target device's Bluetooth address: ").strip()
        send_request(target_address)
    elif choice == "2":
        handle_request()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()

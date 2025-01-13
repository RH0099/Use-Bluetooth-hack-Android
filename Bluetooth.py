import os
import time
from bluetooth import discover_devices
from scapy.all import ARP, Ether, srp
from flask import Flask, request

app = Flask(__name__)

# Bluetooth Scanning Function
def bluetooth_scan():
    print("Scanning for Bluetooth devices...")
    devices = discover_devices(duration=8, lookup_names=True)
    for addr, name in devices:
        print(f"Device Found: {name} ({addr})")

# Network Scanning Function
def network_scan():
    target_ip = "192.168.1.1/24"  # Change based on your network
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    print("Connected Devices:")
    for sent, received in result:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

# File Sharing Function
def file_share():
    print("Starting File Sharing Server...")
    os.system("python -m http.server 8080")

# File Receiving Function
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    return "File uploaded successfully!"

def start_file_receiver():
    print("Starting File Receiving Server...")
    app.run(host='0.0.0.0', port=8080)

# MITM Function
def mitm_proxy():
    print("Starting MITM Proxy...")
    os.system("mitmproxy --mode transparent")

# Main Menu
def main_menu():
    while True:
        print("\nSelect an Option:")
        print("1. Bluetooth Scan")
        print("2. Network Scan")
        print("3. File Sharing")
        print("4. File Receiving")
        print("5. HTTP Traffic Monitoring (MITM)")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bluetooth_scan()
        elif choice == '2':
            network_scan()
        elif choice == '3':
            file_share()
        elif choice == '4':
            start_file_receiver()
        elif choice == '5':
            mitm_proxy()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

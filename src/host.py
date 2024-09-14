#simple code to verify that the device work

import socket

# Device's IP address and port
#DEVICE_IP = '169.254.189.129'  # The IP address you assigned to the device
DEVICE_IP = '10.42.0.61'  # The IP address you assigned to the device
DEVICE_PORT = 1234        # The port number the device is listening on

def main():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            # Connect to the device
            sock.connect((DEVICE_IP, DEVICE_PORT))
            print(f"Connected to {DEVICE_IP}:{DEVICE_PORT}")
            
            # Send data
            message = b'Hello, USB-to-Ethernet device!'
            sock.sendall(message)
            print(f"Sent: {message.decode()}")
            
            # Receive data
            response = sock.recv(4096)
            print(f"Received: {response.decode()}")
        
        except ConnectionError as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

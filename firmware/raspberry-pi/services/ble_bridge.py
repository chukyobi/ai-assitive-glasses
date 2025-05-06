import socket
import bluetooth
import threading

AUDIO_LISTENER_HOST = 'localhost'
AUDIO_LISTENER_PORT = 5000  # Choose a port for communication with audio_listener.py
BLUETOOTH_ADDRESS = "your_bluetooth_address" # Replace with the mobile app's Bluetooth address
BLUETOOTH_UUID = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

def handle_audio_listener_connection(client_sock, client_info):
    print("Accepted audio listener connection from ", client_info)
    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print("Received audio data from audio listener, forwarding to Bluetooth")
            send_to_bluetooth(data)
    except IOError:
        print("Audio listener connection lost")
    finally:
        client_sock.close()

def send_to_bluetooth(data):
    try:
        bluetooth_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        bluetooth_sock.connect((BLUETOOTH_ADDRESS, 1)) # Assuming port 1
        bluetooth_sock.send(data)
        bluetooth_sock.close()
        print("Audio data sent to Bluetooth")
    except Exception as e:
        print(f"Error sending data to Bluetooth: {e}")

def audio_listener_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (AUDIO_LISTENER_HOST, AUDIO_LISTENER_PORT)
    server_sock.bind(server_address)
    server_sock.listen(1)

    print("Waiting for audio listener connection on port %d" % AUDIO_LISTENER_PORT)

    try:
        while True:
            client_sock, client_info = server_sock.accept()
            threading.Thread(target=handle_audio_listener_connection, args=(client_sock, client_info), daemon=True).start()
    except Exception as e:
        print(f"Audio listener server error: {e}")
    finally:
        server_sock.close()

def bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)

    bluetooth.advertise_service(server_sock, "AssistiveGlasses",
                       service_id=BLUETOOTH_UUID,
                       service_classes=[BLUETOOTH_UUID, bluetooth.SERIAL_PORT_CLASS],
                       profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print("Waiting for Bluetooth connection on RFCOMM channel %d" % port)

    try:
        while True:
            client_sock, client_info = server_sock.accept()
            threading.Thread(target=handle_bluetooth_connection, args=(client_sock, client_info), daemon=True).start()
    except Exception as e:
        print(f"Bluetooth server error: {e}")
    finally:
        server_sock.close()

if __name__ == "__main__":
    threading.Thread(target=audio_listener_server, daemon=True).start()
    threading.Thread(target=bluetooth_server, daemon=True).start()
    print("Bluetooth and Audio Listener servers started")

    # Keep the main thread alive
    while True:
        pass

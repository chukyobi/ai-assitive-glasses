import socket
import bluetooth
import threading

DISPLAY_HOST = 'localhost'
DISPLAY_PORT = 12345

def send_text_to_display(text):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((DISPLAY_HOST, DISPLAY_PORT))
            s.sendall(text.encode('utf-8'))
    except Exception as e:
        print(f"Error sending data to display: {e}")

def handle_bluetooth_connection(client_sock, client_info):
    print("Accepted connection from ", client_info)
    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            text = data.decode('utf-8')
            print("Received [%s]" % text)
            send_text_to_display(text)
    except IOError:
        print("Bluetooth connection lost")
    finally:
        client_sock.close()

def bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bluetooth.advertise_service(server_sock, "AssistiveGlasses",
                       service_id=uuid,
                       service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
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
    threading.Thread(target=bluetooth_server, daemon=True).start()
    print("Bluetooth server started")

    # Keep the main thread alive
    while True:
        pass

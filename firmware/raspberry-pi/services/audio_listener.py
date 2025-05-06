import pyaudio
import wave
import noisegain
import opuslib
import socket
import threading
import websocket
import json
import socket
import bluetooth

CLOUD_HOST = 'your_cloud_host'  # Replace with your cloud backend host
CLOUD_PORT = 8080  # Replace with your cloud backend port
BLUETOOTH_ADDRESS = "your_bluetooth_address" # Replace with the mobile app's Bluetooth address
BLUETOOTH_PORT = 1

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
ENCODING_RATE = 48000  # Opus encoding rate
FRAME_SIZE = 20  # Opus frame size in ms

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def send_audio_to_bluetooth(audio_data):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((BLUETOOTH_ADDRESS, BLUETOOTH_PORT))
        sock.send(audio_data)
        sock.close()
        print("Audio data sent to Bluetooth")
    except Exception as e:
        print(f"Error sending audio to Bluetooth: {e}")

def send_audio_to_cloud(audio_data):
    try:
        ws = websocket.create_connection(f"ws://{CLOUD_HOST}:{CLOUD_PORT}/ws/audio")
        ws.send(audio_data, websocket.ABNF.OPCODE_BINARY)
        ws.close()
        print("Audio data sent to cloud")
    except Exception as e:
        print(f"Error sending audio to cloud: {e}")

def process_audio(audio_data):
    # Noise reduction
    # noise_reducer = noisegain.NoiseGainProcessor(rate=RATE)
    # reduced_noise = noise_reducer.run(audio_data)
    # return reduced_noise
    return audio_data # Disable noise reduction for now

def encode_audio(audio_data):
    # Opus encoding
    # enc = opuslib.Encoder(ENCODING_RATE, CHANNELS, 'audio')
    # encoded_data = enc.encode(audio_data)
    # return encoded_data
    return audio_data # Disable encoding for now

def listen_and_send():
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Listening...")

    try:
        while True:
            data = stream.read(CHUNK)
            processed_data = process_audio(data)
            encoded_data = processed_data #encode_audio(processed_data)

            if check_internet_connection():
                send_audio_to_cloud(encoded_data)
            else:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((AUDIO_LISTENER_HOST, 5000)) # Connect to ble_bridge.py
                        s.sendall(encoded_data)
                except Exception as e:
                    print(f"Error sending audio to ble_bridge: {e}")

    except KeyboardInterrupt:
        print("Interrupted")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

if __name__ == "__main__":
    listen_and_send()

import tkinter as tk
import socket
import threading

class DisplayOutput:
    def __init__(self):
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack()
        self.root.title("Assistive Glasses Output")

    def display_text(self, text):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)

    def run(self):
        self.root.mainloop()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 12345)
        server_socket.bind(server_address)
        server_socket.listen(1)

        while True:
            connection, client_address = server_socket.accept()
            try:
                data = connection.recv(1024).decode()
                if data:
                    self.display_text(data)
            finally:
                connection.close()

if __name__ == "__main__":
    display = DisplayOutput()
    threading.Thread(target=display.start_server, daemon=True).start()
    display.run()

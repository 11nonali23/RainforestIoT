import socket
import selectors
import types
import threading
from available_sensors import SENSORS

from command import Command

sel = selectors.DefaultSelector()


class Server(threading.Thread):
    HOST, PORT = "127.0.0.1", 9000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        threading.Thread.__init__(self)
        self.count = 0
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen()
        print(f"Server is listening on {(self.HOST, self.PORT)}")
        self.sock.setblocking(False)
        sel.register(self.sock, selectors.EVENT_READ, data=None)

    def run(self):
        try:
            while True:
                events = sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self._accept_connection(key.fileobj)
                    else:
                        self._serve_connection(key, mask)
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
            sel.close()

    def _accept_connection(self, sock):
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        sel.register(conn, events, data=data)

    def _serve_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                self.count = self.count + 1
                data.outb = self._handle_connection(recv_data, data.outb)
            else:
                print(f"Closing connection to {data.addr}")
                sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(f"Sending result: {data.outb!r} to {data.addr}")
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]
                self._send_close_connection_signal(sock)

    def _handle_connection(self, data, data_outb):
        data = data.decode('utf8')
        command = Command(data, SENSORS)

        if not command.valid:
            data_outb += str.encode("ERROR - invalid command or sensor")

        # Handle the stop iteration exception ?
        sensor = next(
            sensor for sensor in SENSORS
            if sensor._id == command.sensor_id
        )
        result = sensor.do(command)

        data_outb += str.encode(result)
        print("This is the request data:", command)
        print("This is the resulting data:", result)

        return data_outb

    def _send_close_connection_signal(self, sock):
        sock.send(str.encode("\n"))


if __name__ == "__main__":
    s = Server()
    s.start()

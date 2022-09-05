from server.tcp_server import TCPServer
from ui.app import App


if __name__ == "__main__":
    server = TCPServer()
    server.start()

    app = App()
    app.randomize()
    app.update()
    app.mainloop()

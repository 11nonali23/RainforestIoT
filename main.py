from server.tcp_server import Server
from ui.app import App


if __name__ == "__main__":
    server = Server()
    server.start()

    app = App()
    app.randomize()
    app.update()
    app.mainloop()

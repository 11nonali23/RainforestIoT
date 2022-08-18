from server import Server
from ui import App


if __name__ == "__main__":
    server = Server()
    server.start()

    app = App()
    app.update()
    app.mainloop()

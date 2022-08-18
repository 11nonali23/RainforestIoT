from server import Server
from ui import Ui


if __name__ == "__main__":
    server = Server()
    server.start()

    ui = Ui()
    ui.update(server)
    ui.mainloop()
